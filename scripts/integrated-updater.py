#!/usr/bin/env python3
"""
Integrated Updater
Combines brain_helper.py and system-md-updater.py functionality for efficient updates.
This script coordinates all documentation updates to avoid duplication and conflicts.
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Add utils to path for brain_helper import
sys.path.append(str(Path(__file__).parent.parent / 'utils'))

try:
    from brain_helper import BrainHelper
except ImportError as e:
    print(f"Warning: Could not import brain_helper: {e}")
    BrainHelper = None

# Import context monitor
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("context_monitor", str(Path(__file__).parent / "context-monitor.py"))
    context_monitor_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(context_monitor_module)
    ContextMonitor = context_monitor_module.ContextMonitor
    ContextNotifier = getattr(context_monitor_module, 'ContextNotifier', None)
except Exception as e:
    print(f"Warning: Could not import context modules: {e}")
    ContextMonitor = None
    ContextNotifier = None

# Import system updater
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("system_md_updater", str(Path(__file__).parent / "system-md-updater.py"))
    system_updater_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(system_updater_module)
    SystemMDUpdater = system_updater_module.SystemMDUpdater
except Exception as e:
    print(f"Warning: Could not import system updater: {e}")
    SystemMDUpdater = None


class IntegratedUpdater:
    """Coordinates all documentation updates efficiently"""
    
    def __init__(self, root_path: str = "."):
        self.root = Path(root_path)
        self.brain_helper = BrainHelper(str(self.root)) if BrainHelper else None
        self.context_monitor = ContextMonitor(str(self.root)) if ContextMonitor else None
        self.system_updater = SystemMDUpdater(str(self.root)) if SystemMDUpdater else None
        
        # Track what needs updating
        self.update_needed = {
            'index': False,
            'frontmatter': False,
            'context': False,
            'context_sync': False,
            'system': False,
            'infrastructure': False,
            'validation': False
        }
        
        # Shared analysis data
        self.shared_analysis = {}
    
    def analyze_changes(self) -> Dict[str, bool]:
        """Analyze what needs updating based on recent changes"""
        print("🔍 Analyzing what needs updating...")
        
        # Check if files have been modified recently
        recent_threshold = datetime.now().timestamp() - 300  # 5 minutes ago
        
        # Check INDEX.md age
        index_file = self.root / "INDEX.md"
        if not index_file.exists() or index_file.stat().st_mtime < recent_threshold:
            self.update_needed['index'] = True
        
        # Check SYSTEM.md age
        system_file = self.root / "SYSTEM.md"
        if not system_file.exists() or system_file.stat().st_mtime < recent_threshold:
            self.update_needed['system'] = True
        
        # Check for context file changes
        if self.context_monitor:
            changes = self.context_monitor.check_changes()
            if changes:
                self.update_needed['context'] = True
        
        # Check infrastructure overview age
        infra_overview = self.root / "infrastructure" / "INFRASTRUCTURE-OVERVIEW.md"
        if not infra_overview.exists() or infra_overview.stat().st_mtime < recent_threshold:
            self.update_needed['infrastructure'] = True
        
        # Always check frontmatter, context sync, and validation
        self.update_needed['frontmatter'] = True
        self.update_needed['context_sync'] = True
        self.update_needed['validation'] = True
        
        print(f"📊 Update needed: {[k for k, v in self.update_needed.items() if v]}")
        return self.update_needed
    
    def run_shared_analysis(self):
        """Run analysis once and share data between components"""
        print("🔍 Running shared analysis...")
        
        # Get statistics from brain_helper
        self.shared_analysis['stats'] = self.brain_helper.get_statistics()
        self.shared_analysis['high_priority'] = self.brain_helper.get_high_priority()
        
        # Get directory analysis from system_updater
        if self.system_updater:
            self.system_updater.analyze_codebase()
            self.shared_analysis['directories'] = self.system_updater.analysis.get('directories', {})
            self.shared_analysis['file_patterns'] = self.system_updater.analysis.get('file_patterns', {})
        
        print("✅ Shared analysis complete")
    
    def update_index(self):
        """Update INDEX.md using brain_helper"""
        if not self.update_needed['index']:
            print("⏭️  Skipping INDEX.md update (not needed)")
            return
        
        print("📝 Updating INDEX.md...")
        self.brain_helper.sync_index()
        print("✅ INDEX.md updated")
    
    def update_frontmatter(self):
        """Update frontmatter using brain_helper"""
        if not self.update_needed['frontmatter']:
            print("⏭️  Skipping frontmatter update (not needed)")
            return
        
        print("📝 Updating frontmatter...")
        self.brain_helper.update_frontmatter()
        print("✅ Frontmatter updated")
    
    def update_context_monitoring(self):
        """Update context monitoring"""
        if not self.update_needed['context'] or not self.context_monitor:
            print("⏭️  Skipping context monitoring (not needed or not available)")
            return
        
        print("📝 Updating context monitoring...")
        self.context_monitor.run_monitor()
        print("✅ Context monitoring updated")
    
    def sync_context_files(self):
        """Synchronize context files with source directories"""
        if not self.update_needed['context_sync']:
            print("⏭️  Skipping context sync (not needed)")
            return
        
        print("📝 Synchronizing context files...")
        try:
            import subprocess
            result = subprocess.run([
                'python3', 'scripts/context-sync.py', '--sync'
            ], capture_output=True, text=True, cwd=str(self.root))
            
            if result.returncode == 0:
                print("✅ Context files synchronized")
            else:
                print(f"⚠️  Context sync had issues: {result.stderr}")
        except Exception as e:
            print(f"⚠️  Could not sync context files: {e}")
    
    def update_system_md(self):
        """Update SYSTEM.md using system_updater"""
        if not self.update_needed['system'] or not self.system_updater:
            print("⏭️  Skipping SYSTEM.md update (not needed or not available)")
            return
        
        print("📝 Updating SYSTEM.md...")
        self.system_updater.update_system_md()
        print("✅ SYSTEM.md updated")
    
    def update_infrastructure_overview(self):
        """Update infrastructure overview using infrastructure scanner"""
        if not self.update_needed['infrastructure']:
            print("⏭️  Skipping infrastructure overview update (not needed)")
            return
        
        print("📝 Updating infrastructure overview...")
        try:
            import subprocess
            result = subprocess.run([
                'python3', 'scripts/infrastructure-scanner.py', '--scan'
            ], capture_output=True, text=True, cwd=str(self.root))
            
            if result.returncode == 0:
                print("✅ Infrastructure overview updated")
            else:
                print(f"⚠️  Infrastructure update had issues: {result.stderr}")
        except Exception as e:
            print(f"⚠️  Could not update infrastructure overview: {e}")
    
    def validate_system(self):
        """Validate the entire system"""
        if not self.update_needed['validation']:
            print("⏭️  Skipping validation (not needed)")
            return
        
        print("🔍 Validating system...")
        success = self.brain_helper.validate()
        if success:
            print("✅ System validation passed")
        else:
            print("❌ System validation failed")
        return success
    
    def run_full_update(self):
        """Run complete update cycle with shared analysis"""
        print("🚀 Starting integrated update cycle...")
        
        # Run shared analysis once
        self.run_shared_analysis()
        
        # Analyze what needs updating
        self.analyze_changes()
        
        # Run updates in optimal order
        self.update_frontmatter()  # First, ensure all files have proper frontmatter
        self.sync_context_files()  # Then sync context files with source directories
        self.update_index()        # Then update index
        self.update_context_monitoring()  # Then handle context changes
        self.update_system_md()    # Update system documentation
        self.update_infrastructure_overview()  # Update infrastructure overview
        
        # Validate everything
        validation_success = self.validate_system()
        
        print("✅ Integrated update cycle complete")
        return validation_success
    
    def run_quick_update(self):
        """Run quick update for recent changes"""
        print("⚡ Running quick update...")
        
        # Only update what's absolutely necessary
        self.analyze_changes()
        
        if self.update_needed['context'] and self.context_monitor:
            self.update_context_monitoring()
        
        if self.update_needed['index']:
            self.update_index()
        
        print("✅ Quick update complete")
    
    def generate_integration_report(self) -> str:
        """Generate a report showing how components work together"""
        report = [
            "# Integrated Documentation System Report",
            f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*",
            "",
            "## Component Integration",
            "",
            "### Brain Helper (utils/brain_helper.py)",
            "- **Purpose**: Core knowledge base management",
            "- **Functions**: INDEX.md generation, frontmatter updates, validation",
            "- **Data**: File statistics, high-priority items, categorization",
            "",
            "### Context Monitor (scripts/context-monitor.py)",
            "- **Purpose**: Track context file changes",
            "- **Functions**: Change detection, changelog updates, notifications",
            "- **Data**: Context file state, change history",
            "",
            "### System MD Updater (scripts/system-md-updater.py)",
            "- **Purpose**: Keep SYSTEM.md current with codebase",
            "- **Functions**: Structure analysis, documentation generation",
            "- **Data**: Directory purposes, file patterns, automation scripts",
            "",
            "### Integrated Updater (scripts/integrated-updater.py)",
            "- **Purpose**: Coordinate all updates efficiently",
            "- **Functions**: Shared analysis, optimal update ordering, conflict prevention",
            "- **Data**: Update status, shared analysis results",
            "",
            "## Update Workflow",
            "",
            "1. **Shared Analysis**: Run analysis once, share data between components",
            "2. **Change Detection**: Determine what needs updating",
            "3. **Frontmatter Update**: Ensure all files have proper metadata",
            "4. **Index Update**: Update INDEX.md with current structure",
            "5. **Context Monitoring**: Handle context file changes",
            "6. **System Update**: Update SYSTEM.md with current state",
            "7. **Validation**: Verify everything is working correctly",
            "",
            "## Benefits of Integration",
            "",
            "- **Efficiency**: Shared analysis prevents duplicate work",
            "- **Consistency**: All components use the same data",
            "- **Ordering**: Updates run in optimal sequence",
            "- **Conflict Prevention**: Coordinated updates prevent conflicts",
            "- **Performance**: Only update what's actually needed",
            ""
        ]
        
        return '\n'.join(report)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Integrated Documentation Updater")
    parser.add_argument('--full', action='store_true', help='Run full update cycle')
    parser.add_argument('--quick', action='store_true', help='Run quick update for recent changes')
    parser.add_argument('--report', action='store_true', help='Generate integration report')
    parser.add_argument('--root', default='.', help='Root directory path')
    
    args = parser.parse_args()
    
    updater = IntegratedUpdater(args.root)
    
    if args.report:
        report = updater.generate_integration_report()
        report_file = Path(args.root) / 'integration-report.md'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"📊 Integration report saved to {report_file}")
    
    elif args.quick:
        updater.run_quick_update()
    
    elif args.full:
        success = updater.run_full_update()
        sys.exit(0 if success else 1)
    
    else:
        print("Use --full for complete update, --quick for recent changes, or --report for analysis")


if __name__ == "__main__":
    main()
