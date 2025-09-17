#!/usr/bin/env python3
"""
Context File Monitor
Monitors changes to infrastructure.md and tech-stack.md and automatically documents updates.
"""

import os
import sys
import time
import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional
import subprocess

# Import the notifier
sys.path.append(str(Path(__file__).parent))
try:
    from context_notifier import ContextNotifier
except ImportError:
    print("Warning: context_notifier module not found. Notifications will be disabled.")
    ContextNotifier = None

try:
    import frontmatter
except ImportError:
    print("Please install python-frontmatter: pip install python-frontmatter")
    sys.exit(1)


class ContextMonitor:
    """Monitor and document changes to context files"""
    
    def __init__(self, root_path: str = "."):
        self.root = Path(root_path)
        self.context_files = {
            'infrastructure': self.root / 'ai' / 'context' / 'infrastructure.md',
            'tech-stack': self.root / 'ai' / 'context' / 'tech-stack.md'
        }
        self.state_file = self.root / '.context-monitor-state.json'
        self.changelog_file = self.root / 'CHANGELOG.md'
        self.notifier = ContextNotifier(str(self.root)) if ContextNotifier else None
        self.load_state()
    
    def load_state(self):
        """Load previous file states"""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                self.state = json.load(f)
        else:
            self.state = {}
    
    def save_state(self):
        """Save current file states"""
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def get_file_hash(self, file_path: Path) -> Optional[str]:
        """Get MD5 hash of file content"""
        if not file_path.exists():
            return None
        
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    
    def get_file_metadata(self, file_path: Path) -> Dict:
        """Get file metadata including frontmatter"""
        if not file_path.exists():
            return {}
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            return {
                'title': post.metadata.get('title', ''),
                'modified': post.metadata.get('modified', ''),
                'version': post.metadata.get('version', 1),
                'ship_factor': post.metadata.get('ship_factor', 5),
                'size': file_path.stat().st_size,
                'lines': len(post.content.split('\n'))
            }
        except Exception as e:
            print(f"Warning: Could not read metadata from {file_path}: {e}")
            return {
                'title': file_path.stem,
                'modified': datetime.now().isoformat(),
                'version': 1,
                'ship_factor': 5,
                'size': file_path.stat().st_size if file_path.exists() else 0,
                'lines': 0
            }
    
    def check_changes(self) -> Dict[str, Dict]:
        """Check for changes in context files"""
        changes = {}
        
        for name, file_path in self.context_files.items():
            current_hash = self.get_file_hash(file_path)
            previous_hash = self.state.get(name, {}).get('hash')
            
            if current_hash != previous_hash:
                changes[name] = {
                    'file_path': str(file_path),
                    'previous_hash': previous_hash,
                    'current_hash': current_hash,
                    'previous_metadata': self.state.get(name, {}).get('metadata', {}),
                    'current_metadata': self.get_file_metadata(file_path),
                    'timestamp': datetime.now().isoformat()
                }
                
                # Update state
                self.state[name] = {
                    'hash': current_hash,
                    'metadata': changes[name]['current_metadata'],
                    'last_checked': changes[name]['timestamp']
                }
        
        return changes
    
    def generate_changelog_entry(self, changes: Dict[str, Dict]) -> str:
        """Generate changelog entry for context file changes"""
        if not changes:
            return ""
        
        entry_lines = []
        entry_lines.append(f"## Context Updates - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        entry_lines.append("")
        
        for name, change in changes.items():
            file_path = Path(change['file_path'])
            current_meta = change['current_metadata']
            previous_meta = change['previous_metadata']
            
            entry_lines.append(f"### {name.replace('-', ' ').title()} Context")
            entry_lines.append(f"- **File**: `{file_path.relative_to(self.root)}`")
            entry_lines.append(f"- **Title**: {current_meta.get('title', 'N/A')}")
            entry_lines.append(f"- **Version**: {previous_meta.get('version', 1)} → {current_meta.get('version', 1)}")
            entry_lines.append(f"- **Ship Factor**: {previous_meta.get('ship_factor', 5)} → {current_meta.get('ship_factor', 5)}")
            entry_lines.append(f"- **Size**: {previous_meta.get('size', 0)} → {current_meta.get('size', 0)} bytes")
            entry_lines.append(f"- **Lines**: {previous_meta.get('lines', 0)} → {current_meta.get('lines', 0)}")
            
            # Check for significant changes
            significant_changes = []
            if current_meta.get('version', 1) > previous_meta.get('version', 1):
                significant_changes.append("version bump")
            if current_meta.get('ship_factor', 5) != previous_meta.get('ship_factor', 5):
                significant_changes.append("ship factor change")
            if abs(current_meta.get('size', 0) - previous_meta.get('size', 0)) > 100:
                significant_changes.append("significant content change")
            
            if significant_changes:
                entry_lines.append(f"- **Significant Changes**: {', '.join(significant_changes)}")
            
            entry_lines.append("")
        
        return '\n'.join(entry_lines)
    
    def update_changelog(self, changelog_entry: str):
        """Update CHANGELOG.md with new entry"""
        if not changelog_entry:
            return
        
        # Read current changelog
        if self.changelog_file.exists():
            with open(self.changelog_file, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = "# Changelog\n\n"
        
        # Insert new entry after the header
        lines = content.split('\n')
        insert_index = 2  # After "# Changelog" and empty line
        
        # Find the right place to insert (after header, before existing entries)
        for i, line in enumerate(lines):
            if line.startswith('## ') and 'Context Updates' not in line:
                insert_index = i
                break
        
        # Insert the new entry
        new_lines = lines[:insert_index] + [changelog_entry] + lines[insert_index:]
        
        # Write back
        with open(self.changelog_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        
        print(f"✅ Updated {self.changelog_file}")
    
    def create_context_summary(self, changes: Dict[str, Dict]) -> str:
        """Create a summary of context file changes"""
        if not changes:
            return ""
        
        summary_lines = []
        summary_lines.append("# Context Files Update Summary")
        summary_lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
        summary_lines.append("")
        
        for name, change in changes.items():
            file_path = Path(change['file_path'])
            current_meta = change['current_metadata']
            
            summary_lines.append(f"## {name.replace('-', ' ').title()}")
            summary_lines.append(f"- **File**: `{file_path.relative_to(self.root)}`")
            summary_lines.append(f"- **Title**: {current_meta.get('title', 'N/A')}")
            summary_lines.append(f"- **Version**: {current_meta.get('version', 1)}")
            summary_lines.append(f"- **Ship Factor**: {current_meta.get('ship_factor', 5)}")
            summary_lines.append(f"- **Size**: {current_meta.get('size', 0)} bytes")
            summary_lines.append(f"- **Lines**: {current_meta.get('lines', 0)}")
            summary_lines.append("")
        
        return '\n'.join(summary_lines)
    
    def run_monitor(self, watch_mode: bool = False):
        """Run the context monitor"""
        print("🔍 Checking for context file changes...")
        
        changes = self.check_changes()
        
        if changes:
            print(f"📝 Found changes in {len(changes)} context file(s):")
            for name in changes.keys():
                print(f"  - {name}")
            
            # Generate changelog entry
            changelog_entry = self.generate_changelog_entry(changes)
            
            # Update changelog
            self.update_changelog(changelog_entry)
            
            # Create summary
            summary = self.create_context_summary(changes)
            summary_file = self.root / 'CONTEXT-UPDATE-SUMMARY.md'
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(summary)
            print(f"📋 Created summary: {summary_file}")
            
            # Send notifications
            if self.notifier:
                self.notifier.send_notifications(changes)
            
            # Save state
            self.save_state()
            
            print("✅ Context monitoring complete")
            
            # If in watch mode, continue monitoring
            if watch_mode:
                print("👀 Watching for changes... (Press Ctrl+C to stop)")
                try:
                    while True:
                        time.sleep(5)  # Check every 5 seconds
                        new_changes = self.check_changes()
                        if new_changes:
                            print(f"\n🔄 New changes detected at {datetime.now().strftime('%H:%M:%S')}")
                            self.run_monitor(watch_mode=False)
                except KeyboardInterrupt:
                    print("\n👋 Stopping context monitor")
        else:
            print("✅ No changes detected in context files")
            self.save_state()
    
    def force_update(self):
        """Force update of all context files (useful for initial setup)"""
        print("🔄 Force updating context file states...")
        
        for name, file_path in self.context_files.items():
            if file_path.exists():
                current_hash = self.get_file_hash(file_path)
                current_metadata = self.get_file_metadata(file_path)
                
                self.state[name] = {
                    'hash': current_hash,
                    'metadata': current_metadata,
                    'last_checked': datetime.now().isoformat()
                }
                
                print(f"  ✅ Updated state for {name}")
            else:
                print(f"  ⚠️  File not found: {file_path}")
        
        self.save_state()
        print("✅ Force update complete")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Context File Monitor")
    parser.add_argument('--watch', action='store_true', help='Watch mode - continuously monitor files')
    parser.add_argument('--force-update', action='store_true', help='Force update file states')
    parser.add_argument('--root', default='.', help='Root directory path')
    
    args = parser.parse_args()
    
    monitor = ContextMonitor(args.root)
    
    if args.force_update:
        monitor.force_update()
    else:
        monitor.run_monitor(watch_mode=args.watch)


if __name__ == "__main__":
    main()
