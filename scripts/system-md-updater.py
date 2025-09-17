#!/usr/bin/env python3
"""
SYSTEM.md Auto-Updater
Automatically updates SYSTEM.md to reflect the current state of the codebase.
Analyzes repository structure, file patterns, and content to keep documentation current.
"""

import os
import sys
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict

try:
    import frontmatter
except ImportError:
    print("Please install python-frontmatter: pip install python-frontmatter")
    sys.exit(1)


class SystemMDUpdater:
    """Updates SYSTEM.md based on current codebase state"""
    
    def __init__(self, root_path: str = "."):
        self.root = Path(root_path)
        self.system_file = self.root / "SYSTEM.md"
        self.index_file = self.root / "INDEX.md"
        self.changelog_file = self.root / "CHANGELOG.md"
        
        # Load current SYSTEM.md content
        self.current_content = self.load_system_md()
        
        # Analysis results
        self.analysis = {}
    
    def load_system_md(self) -> str:
        """Load current SYSTEM.md content"""
        if self.system_file.exists():
            with open(self.system_file, 'r', encoding='utf-8') as f:
                return f.read()
        return ""
    
    def analyze_codebase(self):
        """Analyze the current codebase structure and content"""
        print("🔍 Analyzing codebase structure...")
        
        self.analysis = {
            'directories': self.analyze_directories(),
            'file_patterns': self.analyze_file_patterns(),
            'frontmatter_stats': self.analyze_frontmatter(),
            'content_patterns': self.analyze_content_patterns(),
            'automation_scripts': self.find_automation_scripts(),
            'configuration_files': self.find_configuration_files(),
            'documentation_files': self.find_documentation_files(),
            'maintenance_commands': self.find_maintenance_commands()
        }
        
        print("✅ Codebase analysis complete")
    
    def analyze_directories(self) -> Dict[str, Dict]:
        """Analyze directory structure and purposes"""
        directories = {}
        
        for item in self.root.iterdir():
            if item.is_dir() and not item.name.startswith('.') and item.name not in ['venv', '__pycache__', 'node_modules']:
                dir_info = {
                    'path': str(item.relative_to(self.root)),
                    'file_count': len(list(item.rglob('*.md'))),
                    'subdirs': [d.name for d in item.iterdir() if d.is_dir()],
                    'purpose': self.infer_directory_purpose(item)
                }
                directories[item.name] = dir_info
        
        return directories
    
    def infer_directory_purpose(self, dir_path: Path) -> str:
        """Infer the purpose of a directory based on its name and contents"""
        name = dir_path.name.lower()
        
        # Check for README files that might explain purpose
        readme_files = list(dir_path.glob('README.md')) + list(dir_path.glob('readme.md'))
        if readme_files:
            try:
                with open(readme_files[0], 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Look for purpose indicators in first few lines
                    first_lines = content.split('\n')[:10]
                    for line in first_lines:
                        if 'purpose' in line.lower() or 'this directory' in line.lower():
                            return line.strip()
            except:
                pass
        
        # Infer from directory name patterns
        purpose_map = {
            'ai': 'AI system components, prompts, and configurations',
            'knowledge': 'Knowledge base with decisions, lessons, and references',
            'systems': 'System definitions, workflows, and rules',
            'tools': 'Tool configurations and integrations',
            'infrastructure': 'Infrastructure definitions and server configurations',
            'commands': 'Command definitions and shortcuts',
            'docs': 'Documentation and guides',
            'scripts': 'Automation and utility scripts',
            'utils': 'Utility functions and helpers'
        }
        
        return purpose_map.get(name, f"Contains {name}-related files")
    
    def analyze_file_patterns(self) -> Dict[str, List[str]]:
        """Analyze file naming patterns and types"""
        patterns = defaultdict(list)
        
        for md_file in self.root.rglob("*.md"):
            if md_file.name in ['SYSTEM.md', 'INDEX.md', 'CHANGELOG.md']:
                continue
            
            relative_path = str(md_file.relative_to(self.root))
            
            # Analyze naming patterns
            if '-' in md_file.stem:
                patterns['kebab-case'].append(relative_path)
            elif '_' in md_file.stem:
                patterns['snake_case'].append(relative_path)
            elif md_file.stem.islower():
                patterns['lowercase'].append(relative_path)
            elif md_file.stem.isupper():
                patterns['UPPERCASE'].append(relative_path)
            
            # Analyze file types by content
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                if '## ' in content and '### ' in content:
                    patterns['structured'].append(relative_path)
                if '```' in content:
                    patterns['code_blocks'].append(relative_path)
                if '---' in content:
                    patterns['frontmatter'].append(relative_path)
                    
            except:
                pass
        
        return dict(patterns)
    
    def analyze_frontmatter(self) -> Dict[str, any]:
        """Analyze frontmatter patterns and statistics"""
        stats = {
            'total_files': 0,
            'with_frontmatter': 0,
            'common_types': defaultdict(int),
            'common_subtypes': defaultdict(int),
            'common_tags': defaultdict(int),
            'ship_factor_distribution': defaultdict(int),
            'missing_fields': defaultdict(int)
        }
        
        required_fields = ['title', 'type', 'subtype', 'tags', 'created', 'modified', 'version', 'ship_factor']
        
        for md_file in self.root.rglob("*.md"):
            if md_file.name in ['SYSTEM.md', 'INDEX.md', 'CHANGELOG.md']:
                continue
            
            stats['total_files'] += 1
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                
                if post.metadata:
                    stats['with_frontmatter'] += 1
                    
                    # Count common values
                    for field, value in post.metadata.items():
                        if field == 'type':
                            stats['common_types'][value] += 1
                        elif field == 'subtype':
                            stats['common_subtypes'][value] += 1
                        elif field == 'tags' and isinstance(value, list):
                            for tag in value:
                                stats['common_tags'][tag] += 1
                        elif field == 'ship_factor':
                            stats['ship_factor_distribution'][value] += 1
                    
                    # Check for missing required fields
                    for field in required_fields:
                        if field not in post.metadata:
                            stats['missing_fields'][field] += 1
                            
            except:
                pass
        
        return stats
    
    def analyze_content_patterns(self) -> Dict[str, List[str]]:
        """Analyze content patterns and structures"""
        patterns = {
            'decision_documents': [],
            'workflow_documents': [],
            'reference_documents': [],
            'configuration_documents': [],
            'tutorial_documents': []
        }
        
        for md_file in self.root.rglob("*.md"):
            if md_file.name in ['SYSTEM.md', 'INDEX.md', 'CHANGELOG.md']:
                continue
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                relative_path = str(md_file.relative_to(self.root))
                
                # Classify by content patterns
                if any(keyword in content.lower() for keyword in ['decision', 'chose', 'selected', 'adopted']):
                    patterns['decision_documents'].append(relative_path)
                if any(keyword in content.lower() for keyword in ['workflow', 'process', 'steps', 'procedure']):
                    patterns['workflow_documents'].append(relative_path)
                if any(keyword in content.lower() for keyword in ['reference', 'cheat sheet', 'quick start']):
                    patterns['reference_documents'].append(relative_path)
                if any(keyword in content.lower() for keyword in ['config', 'setup', 'install', 'configure']):
                    patterns['configuration_documents'].append(relative_path)
                if any(keyword in content.lower() for keyword in ['tutorial', 'guide', 'how to', 'walkthrough']):
                    patterns['tutorial_documents'].append(relative_path)
                    
            except:
                pass
        
        return patterns
    
    def find_automation_scripts(self) -> List[Dict[str, str]]:
        """Find automation scripts and their purposes"""
        scripts = []
        
        for script_file in self.root.rglob("*.py"):
            if 'venv' in str(script_file):
                continue
                
            try:
                with open(script_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract docstring or first comment
                docstring = ""
                if '"""' in content:
                    start = content.find('"""')
                    end = content.find('"""', start + 3)
                    if end > start:
                        docstring = content[start+3:end].strip()
                
                scripts.append({
                    'path': str(script_file.relative_to(self.root)),
                    'purpose': docstring.split('\n')[0] if docstring else "Automation script",
                    'has_main': 'if __name__ == "__main__"' in content
                })
                
            except:
                pass
        
        return scripts
    
    def find_configuration_files(self) -> List[str]:
        """Find configuration files"""
        config_files = []
        
        config_patterns = [
            '*.json', '*.yaml', '*.yml', '*.toml', '*.ini', '*.cfg',
            'Makefile', 'Dockerfile', 'docker-compose.yml', 'package.json',
            'requirements.txt', 'Pipfile', 'pyproject.toml'
        ]
        
        for pattern in config_patterns:
            for config_file in self.root.rglob(pattern):
                if 'venv' not in str(config_file) and '__pycache__' not in str(config_file):
                    config_files.append(str(config_file.relative_to(self.root)))
        
        return sorted(config_files)
    
    def find_documentation_files(self) -> List[Dict[str, str]]:
        """Find documentation files and their purposes"""
        docs = []
        
        for doc_file in self.root.rglob("*.md"):
            if doc_file.name in ['SYSTEM.md', 'INDEX.md', 'CHANGELOG.md']:
                continue
            
            try:
                with open(doc_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract title from frontmatter or first heading
                title = "Untitled"
                if '---' in content:
                    try:
                        post = frontmatter.loads(content)
                        title = post.metadata.get('title', title)
                    except:
                        pass
                else:
                    # Look for first heading
                    lines = content.split('\n')
                    for line in lines:
                        if line.startswith('# '):
                            title = line[2:].strip()
                            break
                
                docs.append({
                    'path': str(doc_file.relative_to(self.root)),
                    'title': title,
                    'size': len(content),
                    'has_code': '```' in content
                })
                
            except:
                pass
        
        return docs
    
    def find_maintenance_commands(self) -> List[str]:
        """Find maintenance commands from Makefile"""
        commands = []
        
        makefile_path = self.root / "Makefile"
        if makefile_path.exists():
            try:
                with open(makefile_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract target names and descriptions
                lines = content.split('\n')
                for line in lines:
                    if ':' in line and '##' in line and not line.startswith('\t'):
                        target = line.split(':')[0].strip()
                        description = line.split('##')[1].strip() if '##' in line else ""
                        commands.append(f"{target}: {description}")
                        
            except:
                pass
        
        return commands
    
    def generate_updated_system_md(self) -> str:
        """Generate updated SYSTEM.md content"""
        print("📝 Generating updated SYSTEM.md...")
        
        # Start with the header
        content = [
            "# AI Brain Navigation System",
            "",
            "You have access to a knowledge base organized as markdown files. This document defines how to navigate and use this system.",
            "",
            "*Last updated: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "*",
            ""
        ]
        
        # Add structure convention based on current directories
        content.extend(self.generate_structure_section())
        
        # Add reading files section
        content.extend(self.generate_reading_section())
        
        # Add CRUD operations
        content.extend(self.generate_crud_section())
        
        # Add frontmatter schema
        content.extend(self.generate_frontmatter_section())
        
        # Add priority rules
        content.extend(self.generate_priority_section())
        
        # Add quick lookup patterns
        content.extend(self.generate_lookup_section())
        
        # Add naming conventions
        content.extend(self.generate_naming_section())
        
        # Add content guidelines
        content.extend(self.generate_content_guidelines())
        
        # Add integration notes
        content.extend(self.generate_integration_section())
        
        # Add automation section
        content.extend(self.generate_automation_section())
        
        # Add maintenance tasks
        content.extend(self.generate_maintenance_section())
        
        return '\n'.join(content)
    
    def generate_structure_section(self) -> List[str]:
        """Generate structure convention section"""
        content = [
            "## Structure Convention",
            "",
            "- All files are markdown with YAML frontmatter",
            "- Paths indicate type and purpose:",
        ]
        
        # Add current directory purposes
        for dir_name, dir_info in self.analysis['directories'].items():
            content.append(f"  - `{dir_info['path']}/` = {dir_info['purpose']}")
        
        content.extend([
            "- Newer files override older ones (check `modified` date in frontmatter)",
            "- References use relative paths: `[link text](knowledge/decisions/example.md)`",
            ""
        ])
        
        return content
    
    def generate_reading_section(self) -> List[str]:
        """Generate reading files section"""
        return [
            "## Reading Files",
            "",
            "1. **Check INDEX.md first** for quick lookups and navigation",
            "2. **Navigate by path**: `category/subcategory/filename.md`",
            "3. **Parse frontmatter** for metadata (YAML between `---` markers)",
            "4. **Use tags** for cross-references and semantic search",
            "5. **Check deprecated status** before using any content",
            ""
        ]
    
    def generate_crud_section(self) -> List[str]:
        """Generate CRUD operations section"""
        return [
            "## CRUD Operations",
            "",
            "### CREATE",
            "- Add to appropriate folder based on content type",
            "- Include complete frontmatter (see schema below)",
            "- Update INDEX.md with reference to new file",
            "- Use descriptive, kebab-case filenames",
            "",
            "### READ",
            "- Access directly by path",
            "- Search by tags in frontmatter",
            "- Use INDEX.md for categorized browsing",
            "- Check `ship_factor` for implementation priority",
            "",
            "### UPDATE",
            "- Increment `version` in frontmatter",
            "- Update `modified` timestamp",
            "- Keep change history in content if significant",
            "- Update INDEX.md if title or priority changes",
            "",
            "### DELETE",
            "- Set `deprecated: true` in frontmatter",
            "- Add `deprecated_date` and `deprecated_reason`",
            "- DO NOT remove files (maintain history)",
            "- Update INDEX.md to show deprecation",
            ""
        ]
    
    def generate_frontmatter_section(self) -> List[str]:
        """Generate frontmatter schema section"""
        return [
            "## Frontmatter Schema",
            "",
            "```yaml",
            "title: Human-readable title (required)",
            "type: knowledge|behavior|system|tool (required)",
            "subtype: specific subcategory (required)",
            "tags: [searchable, tags, here] (required)",
            "created: ISO-8601 date (required)",
            "modified: ISO-8601 date (required)",
            "version: integer starting at 1 (required)",
            "ship_factor: 1-10 scale (10 = ship immediately)",
            "deprecated: boolean (default: false)",
            "deprecated_date: ISO-8601 date (if deprecated)",
            "deprecated_reason: explanation (if deprecated)",
            "supersedes: path/to/previous/version.md",
            "references: ",
            "  - relative/path/to/related.md",
            "  - another/related/file.md",
            "```",
            ""
        ]
    
    def generate_priority_section(self) -> List[str]:
        """Generate priority rules section"""
        return [
            "## Priority Rules",
            "",
            "1. **Ship Factor Scale**:",
            "   - 9-10: Implement immediately, blocking issue",
            "   - 7-8: High priority, implement this week",
            "   - 5-6: Normal priority, implement this sprint",
            "   - 3-4: Low priority, nice to have",
            "   - 1-2: Future consideration, research only",
            "",
            "2. **Deprecated Content**: ",
            "   - Files with `deprecated: true` should be ignored",
            "   - Check `supersedes` field for replacement",
            "",
            "3. **Version Conflicts**:",
            "   - Use highest version number when multiple exist",
            "   - Check `modified` date as tiebreaker",
            ""
        ]
    
    def generate_lookup_section(self) -> List[str]:
        """Generate quick lookup patterns section"""
        content = [
            "## Quick Lookup Patterns",
            ""
        ]
        
        # Add patterns based on current content analysis
        if self.analysis['content_patterns']['decision_documents']:
            content.append("- **Recent decisions**: Sort by `modified` in `knowledge/decisions/`")
        if self.analysis['content_patterns']['workflow_documents']:
            content.append("- **Active workflows**: `systems/workflows/` where `deprecated: false`")
        if self.analysis['content_patterns']['reference_documents']:
            content.append("- **Quick references**: `knowledge/references/` with tag `reference`")
        
        content.extend([
            "- **High-priority items**: Search for `ship_factor: [8-10]`",
            "- **Anti-patterns**: Check `knowledge/lessons/` with tag `anti-pattern`",
            "- **Current tech stack**: `tools/integrations/` with tag `active`",
            ""
        ])
        
        return content
    
    def generate_naming_section(self) -> List[str]:
        """Generate naming conventions section"""
        content = [
            "## Naming Conventions",
            "",
            "### File Names",
            "- Use kebab-case: `why-we-chose-dify.md`",
            "- Be descriptive but concise",
            "- Include date for time-sensitive content: `2024-q1-roadmap.md`",
            "- Avoid generic names: use `react-component-structure.md` not `structure.md`",
            "",
            "### Folder Organization",
            "- Keep hierarchy shallow (max 3 levels)",
            "- Group by function, not by project",
            "- Use plural for folder names: `decisions` not `decision`",
            ""
        ]
        
        # Add current naming patterns if they exist
        if self.analysis['file_patterns']:
            content.extend([
                "### Current Patterns",
            ])
            for pattern, files in self.analysis['file_patterns'].items():
                if files:
                    content.append(f"- **{pattern}**: {len(files)} files")
            content.append("")
        
        return content
    
    def generate_content_guidelines(self) -> List[str]:
        """Generate content guidelines section"""
        return [
            "## Content Guidelines",
            "",
            "### Decision Documents",
            "- Include: Context, Decision, Reasoning, Trade-offs, Upgrade triggers",
            "- Tag with: technology names, architectural patterns",
            "- Reference: related decisions, lessons learned",
            "",
            "### Lesson Documents",
            "- Include: What happened, What we learned, What to do instead",
            "- Tag with: `lesson`, `anti-pattern` (if applicable)",
            "- Reference: decisions that led to this lesson",
            "",
            "### Workflow Documents",
            "- Include: Prerequisites, Steps, Validation, Rollback procedure",
            "- Tag with: frequency (`daily`, `weekly`), area (`deployment`, `review`)",
            "- Reference: tools used, related workflows",
            ""
        ]
    
    def generate_integration_section(self) -> List[str]:
        """Generate integration notes section"""
        return [
            "## Integration Notes",
            "",
            "### For Dify",
            "- Point to this folder as knowledge base",
            "- Use tags for retrieval filtering",
            "- Ship factor becomes relevance score",
            "",
            "### For MCP Servers",
            "- Read SYSTEM.md first for context",
            "- Use INDEX.md for navigation",
            "- Parse frontmatter before content",
            "",
            "### For Human Editors",
            "- Edit with any text editor",
            "- Compatible with Obsidian, VS Code, etc.",
            "- Preview supported on GitHub",
            ""
        ]
    
    def generate_automation_section(self) -> List[str]:
        """Generate automation section based on current scripts"""
        content = [
            "## Automation & Scripts",
            ""
        ]
        
        if self.analysis['automation_scripts']:
            content.append("### Available Scripts")
            for script in self.analysis['automation_scripts']:
                content.append(f"- **{script['path']}**: {script['purpose']}")
            content.append("")
        
        if self.analysis['maintenance_commands']:
            content.append("### Maintenance Commands")
            for command in self.analysis['maintenance_commands'][:10]:  # Limit to first 10
                content.append(f"- `{command}`")
            content.append("")
        
        if self.analysis['configuration_files']:
            content.append("### Configuration Files")
            for config in self.analysis['configuration_files'][:10]:  # Limit to first 10
                content.append(f"- `{config}`")
            content.append("")
        
        return content
    
    def generate_maintenance_section(self) -> List[str]:
        """Generate maintenance tasks section"""
        return [
            "## Maintenance Tasks",
            "",
            "### Daily",
            "- Update INDEX.md with new additions",
            "- Check for deprecated items past expiry",
            "- Verify changelog is updated with recent changes",
            "- Review context file changes in CHANGELOG.md",
            "",
            "### Weekly",
            "- Review high ship factor items",
            "- Archive completed decisions",
            "- Update tool configurations",
            "- Consolidate changelog entries",
            "- Check context file monitoring logs",
            "",
            "### Monthly",
            "- Consolidate duplicate knowledge",
            "- Update deprecated references",
            "- Review and clean up tags",
            "- Release new version and update changelog",
            "- Review context file change patterns",
            ""
        ]
    
    def update_system_md(self):
        """Update SYSTEM.md with current codebase analysis"""
        print("🔄 Updating SYSTEM.md...")
        
        # Generate new content
        new_content = self.generate_updated_system_md()
        
        # Write to file
        with open(self.system_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ SYSTEM.md updated successfully")
    
    def generate_analysis_report(self) -> str:
        """Generate a detailed analysis report"""
        report = [
            "# Codebase Analysis Report",
            f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*",
            "",
            "## Directory Structure",
            ""
        ]
        
        for dir_name, dir_info in self.analysis['directories'].items():
            report.append(f"### {dir_name}")
            report.append(f"- **Path**: `{dir_info['path']}`")
            report.append(f"- **Purpose**: {dir_info['purpose']}")
            report.append(f"- **Files**: {dir_info['file_count']} markdown files")
            if dir_info['subdirs']:
                report.append(f"- **Subdirectories**: {', '.join(dir_info['subdirs'])}")
            report.append("")
        
        report.extend([
            "## File Statistics",
            "",
            f"- **Total files analyzed**: {self.analysis['frontmatter_stats']['total_files']}",
            f"- **Files with frontmatter**: {self.analysis['frontmatter_stats']['with_frontmatter']}",
            "",
            "### Common Types",
            ""
        ])
        
        for type_name, count in sorted(self.analysis['frontmatter_stats']['common_types'].items(), key=lambda x: x[1], reverse=True):
            report.append(f"- **{type_name}**: {count} files")
        
        report.extend([
            "",
            "### Common Tags",
            ""
        ])
        
        for tag, count in sorted(self.analysis['frontmatter_stats']['common_tags'].items(), key=lambda x: x[1], reverse=True)[:10]:
            report.append(f"- **{tag}**: {count} files")
        
        return '\n'.join(report)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="SYSTEM.md Auto-Updater")
    parser.add_argument('--update', action='store_true', help='Update SYSTEM.md')
    parser.add_argument('--analyze', action='store_true', help='Generate analysis report')
    parser.add_argument('--report-file', default='codebase-analysis-report.md', help='Output file for analysis report')
    parser.add_argument('--root', default='.', help='Root directory path')
    
    args = parser.parse_args()
    
    updater = SystemMDUpdater(args.root)
    updater.analyze_codebase()
    
    if args.analyze:
        report = updater.generate_analysis_report()
        report_file = Path(args.root) / args.report_file
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"📊 Analysis report saved to {report_file}")
    
    if args.update:
        updater.update_system_md()
    
    if not args.analyze and not args.update:
        print("Use --update to update SYSTEM.md or --analyze to generate analysis report")


if __name__ == "__main__":
    main()
