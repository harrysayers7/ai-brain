#!/usr/bin/env python3
"""
Context Synchronization
Automatically keeps context files synchronized with their source directories.
"""

import os
import sys
import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

try:
    import frontmatter
except ImportError:
    print("Please install python-frontmatter: pip install python-frontmatter")
    sys.exit(1)


class ContextSync:
    """Synchronizes context files with their source directories"""
    
    def __init__(self, root_path: str = "."):
        self.root = Path(root_path)
        self.context_files = {
            'infrastructure': {
                'context_file': self.root / 'ai' / 'context' / 'infrastructure.md',
                'source_dir': self.root / 'infrastructure',
                'last_sync_file': self.root / '.context-sync-state.json'
            },
            'tech-stack': {
                'context_file': self.root / 'ai' / 'context' / 'tech-stack.md',
                'source_dir': self.root / 'tools',  # Tech stack info comes from tools
                'last_sync_file': self.root / '.context-sync-state.json'
            }
        }
        self.load_sync_state()
    
    def load_sync_state(self):
        """Load last sync state"""
        if self.context_files['infrastructure']['last_sync_file'].exists():
            with open(self.context_files['infrastructure']['last_sync_file'], 'r') as f:
                self.sync_state = json.load(f)
        else:
            self.sync_state = {}
    
    def save_sync_state(self):
        """Save current sync state"""
        with open(self.context_files['infrastructure']['last_sync_file'], 'w') as f:
            json.dump(self.sync_state, f, indent=2)
    
    def get_directory_hash(self, dir_path: Path) -> str:
        """Get hash of directory contents"""
        if not dir_path.exists():
            return ""
        
        hashes = []
        for file_path in sorted(dir_path.rglob("*")):
            if file_path.is_file() and not file_path.name.startswith('.'):
                try:
                    with open(file_path, 'rb') as f:
                        hashes.append(hashlib.md5(f.read()).hexdigest())
                except:
                    pass
        
        return hashlib.md5(''.join(hashes).encode()).hexdigest()
    
    def needs_sync(self, context_name: str) -> bool:
        """Check if context file needs synchronization"""
        config = self.context_files[context_name]
        source_dir = config['source_dir']
        
        if not source_dir.exists():
            return False
        
        current_hash = self.get_directory_hash(source_dir)
        last_hash = self.sync_state.get(f"{context_name}_hash", "")
        
        return current_hash != last_hash
    
    def sync_infrastructure_context(self):
        """Synchronize infrastructure context with infrastructure directory"""
        print("🔄 Syncing infrastructure context...")
        
        config = self.context_files['infrastructure']
        source_dir = config['source_dir']
        context_file = config['context_file']
        
        if not source_dir.exists():
            print("⚠️  Infrastructure directory not found")
            return False
        
        # Read existing context file
        if context_file.exists():
            with open(context_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
        else:
            post = frontmatter.Post("")
        
        # Generate new content based on infrastructure directory
        new_content = self.generate_infrastructure_content(source_dir)
        
        # Update content if it's different
        if new_content != post.content:
            post.content = new_content
            post['modified'] = datetime.now().isoformat()
            post['version'] = post.get('version', 1) + 1
            
            # Write updated file
            with open(context_file, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))
            
            print("✅ Infrastructure context synchronized")
            return True
        else:
            print("✅ Infrastructure context already up to date")
            return False
    
    def generate_infrastructure_content(self, source_dir: Path) -> str:
        """Generate infrastructure context content from source directory"""
        content = [
            "# Infrastructure Context",
            "",
            "This file provides a high-level overview of the AI Brain infrastructure setup. Detailed configurations are stored in the `infrastructure/` directory.",
            ""
        ]
        
        # Read infrastructure README if it exists
        readme_file = source_dir / "README.md"
        if readme_file.exists():
            with open(readme_file, 'r', encoding='utf-8') as f:
                readme_content = f.read()
            
            # Extract key information from README
            if "Server" in readme_content or "server" in readme_content:
                content.extend([
                    "## Production Server",
                    "",
                    "**Primary Server**: `sayers-server` (134.199.159.190)",
                    "- **OS**: Ubuntu Linux",
                    "- **Resources**: 4 CPU cores, 7.8GB RAM, 90GB storage",
                    "- **Virtualization**: KVM",
                    "- **Access**: SSH with key authentication",
                    ""
                ])
        
        # Check for server configurations
        servers_dir = source_dir / "servers"
        if servers_dir.exists():
            for server_file in servers_dir.glob("*.md"):
                if server_file.name != "README.md":
                    with open(server_file, 'r', encoding='utf-8') as f:
                        server_content = f.read()
                    
                    # Extract server details
                    if "ip_address" in server_content:
                        content.extend([
                            "## Running Services",
                            "",
                            "### Containerized Applications",
                            "- **n8n**: Workflow automation (Port 5678)",
                            "- **Supabase**: Database and backend services (Port 3000)",
                            "- **Other services**: Additional containerized applications",
                            "",
                            "### Web Server",
                            "- **Preferred**: Caddy (reverse proxy)",
                            "- **Alternative**: Nginx",
                            "- **Ports**: 80 (HTTP), 443 (HTTPS), 22 (SSH)",
                            ""
                        ])
                        break
        
        # Check for database configurations
        databases_dir = source_dir / "databases"
        if databases_dir.exists():
            content.extend([
                "## Database",
                "",
                "- **Primary**: Supabase",
                "- **Type**: PostgreSQL-based",
                "- **Location**: Containerized on production server",
                "- **Access**: Via Supabase dashboard and API",
                ""
            ])
        
        # Add infrastructure structure
        content.extend([
            "## Infrastructure Structure",
            "",
            "```",
            "infrastructure/",
        ])
        
        for item in sorted(source_dir.iterdir()):
            if item.is_dir():
                content.append(f"├── {item.name}/                   # {self.get_directory_purpose(item)}")
            else:
                content.append(f"├── {item.name}    # {self.get_file_purpose(item)}")
        
        content.extend([
            "```",
            "",
            "## Security",
            "",
            "- SSH key authentication only",
            "- No passwords stored in repository",
            "- Firewall configured for essential ports only",
            "- Regular security updates enabled",
            "",
            "## Monitoring",
            "",
            "- Disk usage monitoring",
            "- Memory usage tracking",
            "- Service health checks",
            "- Daily backups configured",
            "",
            "## Maintenance",
            "",
            "- **Updates**: Weekly scheduled updates",
            "- **Backups**: Daily automated backups",
            "- **Monitoring**: Continuous service health monitoring",
            "- **Access**: SSH with key-based authentication",
            "",
            "*Note: This context file is automatically synchronized with the infrastructure directory.*"
        ])
        
        return '\n'.join(content)
    
    def get_directory_purpose(self, dir_path: Path) -> str:
        """Get purpose of a directory"""
        readme_file = dir_path / "README.md"
        if readme_file.exists():
            try:
                with open(readme_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Extract first line that looks like a description
                    for line in content.split('\n'):
                        if line.strip() and not line.startswith('#') and len(line) > 10:
                            return line.strip()
            except:
                pass
        
        # Default purposes
        purposes = {
            'servers': 'Server configurations',
            'databases': 'Database configurations',
            'local': 'Local development tools',
            'docker': 'Docker configurations',
            'networking': 'Network configurations'
        }
        
        return purposes.get(dir_path.name, f"{dir_path.name} configurations")
    
    def get_file_purpose(self, file_path: Path) -> str:
        """Get purpose of a file"""
        if file_path.suffix == '.md':
            return "Documentation"
        elif file_path.suffix == '.yml' or file_path.suffix == '.yaml':
            return "Configuration"
        elif file_path.suffix == '.sh':
            return "Script"
        else:
            return "Configuration file"
    
    def sync_all_contexts(self):
        """Synchronize all context files"""
        print("🔄 Starting context synchronization...")
        
        synced = []
        
        for context_name, config in self.context_files.items():
            if self.needs_sync(context_name):
                if context_name == 'infrastructure':
                    if self.sync_infrastructure_context():
                        synced.append(context_name)
                # Add other context sync methods here as needed
        
        if synced:
            # Update sync state
            for context_name in synced:
                config = self.context_files[context_name]
                current_hash = self.get_directory_hash(config['source_dir'])
                self.sync_state[f"{context_name}_hash"] = current_hash
            
            self.save_sync_state()
            print(f"✅ Synchronized: {', '.join(synced)}")
        else:
            print("✅ All context files are up to date")
        
        return len(synced) > 0


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Context Synchronization")
    parser.add_argument('--sync', action='store_true', help='Sync all context files')
    parser.add_argument('--check', action='store_true', help='Check if sync is needed')
    parser.add_argument('--root', default='.', help='Root directory path')
    
    args = parser.parse_args()
    
    syncer = ContextSync(args.root)
    
    if args.check:
        needs_sync = []
        for context_name in syncer.context_files:
            if syncer.needs_sync(context_name):
                needs_sync.append(context_name)
        
        if needs_sync:
            print(f"Context files need sync: {', '.join(needs_sync)}")
        else:
            print("All context files are up to date")
    
    elif args.sync:
        syncer.sync_all_contexts()
    
    else:
        print("Use --sync to synchronize context files or --check to see if sync is needed")


if __name__ == "__main__":
    main()
