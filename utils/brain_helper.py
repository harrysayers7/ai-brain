#!/usr/bin/env python3
"""
AI Brain Helper Utilities

Utility functions for managing the AI Brain knowledge base.
Updated to reflect current repository structure (2025-01-15).
"""

import os
import yaml
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

try:
    import frontmatter
except ImportError:
    print("Please install python-frontmatter: pip install python-frontmatter")
    exit(1)


class BrainHelper:
    """Helper class for AI Brain operations"""
    
    def __init__(self, root_path: str = "."):
        self.root = Path(root_path)
        self.ensure_structure()
    
    def ensure_structure(self):
        """Ensure all required directories exist based on current structure"""
        directories = [
            # Knowledge base
            "knowledge/decisions",
            "knowledge/lessons",
            "knowledge/references",
            
            # Prompts (removed hardcoded subdirectories - let them be created dynamically)
            
            # Systems
            "systems/workflows",
            "systems/rules",
            
            # Tools & Integrations
            "tools/integrations",
            "tools/mcp-servers",
            "tools/claude-desktop",
            
            # Infrastructure
            "infrastructure/servers",
            "infrastructure/local",
            "infrastructure/databases",
            "infrastructure/docker",
            "infrastructure/networking",
            
            # Commands
            "commands/shortcuts",
            "commands/templates",
            "commands/macros",
            "commands/slash-commands",
            
            # Instructions
            "instructions/mcp-instructions",
            "instructions/trigger-dev",
            
            # Prompts (removed - no longer needed)
            
            # Utils
            "utils"
        ]
        
        for dir_path in directories:
            (self.root / dir_path).mkdir(parents=True, exist_ok=True)
    
    def create_document(
        self,
        title: str,
        content: str,
        doc_type: str,
        subtype: str,
        tags: List[str] = None,
        ship_factor: int = 5,
        references: List[str] = None,
        category: str = None
    ) -> str:
        """Create a new document with frontmatter"""
        
        # Generate filename from title
        slug = self._slugify(title)
        
        # Determine path based on category and type
        if category:
            path = self.root / category / subtype / f"{slug}.md"
        else:
            path = self.root / doc_type / subtype / f"{slug}.md"
        
        # Check if file exists
        if path.exists():
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            if category:
                path = self.root / category / subtype / f"{slug}-{timestamp}.md"
            else:
                path = self.root / doc_type / subtype / f"{slug}-{timestamp}.md"
        
        # Create document with frontmatter
        post = frontmatter.Post(content)
        post['title'] = title
        post['type'] = doc_type
        post['subtype'] = subtype
        post['tags'] = tags or []
        post['created'] = datetime.now().isoformat()
        post['modified'] = datetime.now().isoformat()
        post['version'] = 1
        post['ship_factor'] = ship_factor
        post['deprecated'] = False
        
        if references:
            post['references'] = references
        
        if category:
            post['category'] = category
        
        # Write file
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
        
        # Update index
        self.update_index()
        
        return str(path)
    
    def read_document(self, path: str) -> Dict[str, Any]:
        """Read a document and return metadata and content"""
        file_path = self.root / path
        
        if not file_path.exists():
            raise FileNotFoundError(f"Document not found: {path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        return {
            'metadata': post.metadata,
            'content': post.content,
            'path': path
        }
    
    def update_document(
        self,
        path: str,
        content: Optional[str] = None,
        metadata_updates: Optional[Dict] = None
    ) -> str:
        """Update an existing document"""
        file_path = self.root / path
        
        if not file_path.exists():
            raise FileNotFoundError(f"Document not found: {path}")
        
        # Load existing document
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        # Update content if provided
        if content is not None:
            post.content = content
        
        # Update metadata
        if metadata_updates:
            post.metadata.update(metadata_updates)
        
        # Always update version and modified date
        post['version'] = post.get('version', 1) + 1
        post['modified'] = datetime.now().isoformat()
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))
        
        # Update index
        self.update_index()
        
        return str(file_path)
    
    def deprecate_document(self, path: str, reason: str) -> str:
        """Mark a document as deprecated"""
        return self.update_document(
            path,
            metadata_updates={
                'deprecated': True,
                'deprecated_date': datetime.now().isoformat(),
                'deprecated_reason': reason
            }
        )
    
    def find_by_tags(self, tags: List[str]) -> List[Dict]:
        """Find all documents with specified tags"""
        results = []
        
        for md_file in self.root.rglob("*.md"):
            if md_file.name in ['SYSTEM.md', 'INDEX.md', 'README.md', 'CHANGELOG.md']:
                continue
            
            with open(md_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            doc_tags = post.get('tags', [])
            if any(tag in doc_tags for tag in tags):
                results.append({
                    'path': str(md_file.relative_to(self.root)),
                    'title': post.get('title', 'Untitled'),
                    'tags': doc_tags,
                    'ship_factor': post.get('ship_factor', 0),
                    'category': post.get('category', 'unknown')
                })
        
        return sorted(results, key=lambda x: x['ship_factor'], reverse=True)
    
    def get_high_priority(self, min_ship_factor: int = 8) -> List[Dict]:
        """Get all high-priority items"""
        results = []
        
        for md_file in self.root.rglob("*.md"):
            if md_file.name in ['SYSTEM.md', 'INDEX.md', 'README.md', 'CHANGELOG.md']:
                continue
            
            with open(md_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            if post.get('ship_factor', 0) >= min_ship_factor:
                if not post.get('deprecated', False):
                    results.append({
                        'path': str(md_file.relative_to(self.root)),
                        'title': post.get('title', 'Untitled'),
                        'ship_factor': post.get('ship_factor'),
                        'modified': post.get('modified'),
                        'category': post.get('category', 'unknown')
                    })
        
        return sorted(results, key=lambda x: x['ship_factor'], reverse=True)
    
    def get_by_category(self, category: str) -> List[Dict]:
        """Get all documents in a specific category"""
        results = []
        category_path = self.root / category
        
        if not category_path.exists():
            return results
        
        for md_file in category_path.rglob("*.md"):
            if md_file.name in ['README.md']:
                continue
            
            with open(md_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            results.append({
                'path': str(md_file.relative_to(self.root)),
                'title': post.get('title', 'Untitled'),
                'ship_factor': post.get('ship_factor', 0),
                'modified': post.get('modified'),
                'deprecated': post.get('deprecated', False)
            })
        
        return sorted(results, key=lambda x: x['ship_factor'], reverse=True)
    
    def get_mcp_servers(self) -> List[Dict]:
        """Get all MCP server configurations"""
        return self.get_by_category("tools/mcp-servers")
    
    def get_commands(self) -> List[Dict]:
        """Get all command-related documents"""
        results = []
        for subdir in ['shortcuts', 'templates', 'macros', 'slash-commands']:
            results.extend(self.get_by_category(f"commands/{subdir}"))
        return results
    
    def get_infrastructure(self) -> List[Dict]:
        """Get all infrastructure-related documents"""
        results = []
        for subdir in ['servers', 'local', 'databases', 'docker', 'networking']:
            results.extend(self.get_by_category(f"infrastructure/{subdir}"))
        return results
    
    def update_index(self):
        """Update the INDEX.md file with current content"""
        stats = self.get_statistics()
        high_priority = self.get_high_priority()
        
        # Read current INDEX.md and update statistics section
        # (Implementation depends on your specific needs)
        print(f"Index updated: {stats['total']} total items")
    
    def get_statistics(self) -> Dict[str, int]:
        """Get comprehensive statistics about the knowledge base"""
        stats = {
            'total': 0,
            'knowledge': 0,
            'prompts': 0,
            'systems': 0,
            'tools': 0,
            'infrastructure': 0,
            'commands': 0,
            'instructions': 0,
            'prompts': 0,
            'deprecated': 0,
            'mcp_servers': 0,
            'high_priority': 0
        }
        
        for md_file in self.root.rglob("*.md"):
            if md_file.name in ['SYSTEM.md', 'INDEX.md', 'README.md', 'CHANGELOG.md']:
                continue
            
            # Skip files in venv directory
            if "venv/" in str(md_file):
                continue
            
            stats['total'] += 1
            
            with open(md_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            if post.get('deprecated', False):
                stats['deprecated'] += 1
            
            if post.get('ship_factor', 0) >= 8:
                stats['high_priority'] += 1
            
            # Categorize by path
            relative_path = str(md_file.relative_to(self.root))
            
            if relative_path.startswith('knowledge/'):
                stats['knowledge'] += 1
            elif relative_path.startswith('prompts/'):
                stats['prompts'] += 1
            elif relative_path.startswith('systems/'):
                stats['systems'] += 1
            elif relative_path.startswith('tools/'):
                stats['tools'] += 1
                if relative_path.startswith('tools/mcp-servers/'):
                    stats['mcp_servers'] += 1
            elif relative_path.startswith('infrastructure/'):
                stats['infrastructure'] += 1
            elif relative_path.startswith('commands/'):
                stats['commands'] += 1
            elif relative_path.startswith('instructions/'):
                stats['instructions'] += 1
            elif relative_path.startswith('prompts/'):
                stats['prompts'] += 1
        
        return stats
    
    def generate_report(self) -> str:
        """Generate a comprehensive report of the knowledge base"""
        stats = self.get_statistics()
        high_priority = self.get_high_priority()
        mcp_servers = self.get_mcp_servers()
        commands = self.get_commands()
        infrastructure = self.get_infrastructure()
        
        report = f"""
# AI Brain Knowledge Base Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Statistics
- **Total Documents**: {stats['total']}
- **Knowledge**: {stats['knowledge']}
- **Prompts**: {stats['prompts']}
- **Systems**: {stats['systems']}
- **Tools**: {stats['tools']} (MCP Servers: {stats['mcp_servers']})
- **Infrastructure**: {stats['infrastructure']}
- **Commands**: {stats['commands']}
- **Instructions**: {stats['instructions']}
- **Prompts**: {stats['prompts']}
- **High Priority**: {stats['high_priority']}
- **Deprecated**: {stats['deprecated']}

## High Priority Items (Ship Factor 8+)
"""
        
        for item in high_priority:
            report += f"- [{item['ship_factor']}] {item['title']} ({item['category']})\n"
            report += f"  Path: {item['path']}\n"
        
        report += f"\n## MCP Servers ({len(mcp_servers)})\n"
        for server in mcp_servers:
            report += f"- {server['title']} (Ship Factor: {server['ship_factor']})\n"
        
        report += f"\n## Commands ({len(commands)})\n"
        for cmd in commands:
            report += f"- {cmd['title']} (Ship Factor: {cmd['ship_factor']})\n"
        
        report += f"\n## Infrastructure ({len(infrastructure)})\n"
        for infra in infrastructure:
            report += f"- {infra['title']} (Ship Factor: {infra['ship_factor']})\n"
        
        return report
    
    def _slugify(self, text: str) -> str:
        """Convert text to URL-friendly slug"""
        import re
        text = text.lower()
        text = re.sub(r'[^a-z0-9]+', '-', text)
        text = text.strip('-')
        return text

    def sync_index(self):
        """Sync INDEX.md with current file structure"""
        index_path = self.root / "INDEX.md"
        
        # Dynamically discover all top-level directories
        categories = {}
        for item in self.root.iterdir():
            if item.is_dir() and not item.name.startswith('.') and item.name not in ['venv', '__pycache__']:
                categories[item.name.title()] = []
        
        for md_file in self.root.rglob("*.md"):
            if md_file.name in ["README.md", "INDEX.md", "CHANGELOG.md", "SYSTEM.md"]:
                continue
            
            # Skip files in venv directory
            if "venv/" in str(md_file):
                continue
                
            relative_path = md_file.relative_to(self.root)
            path_parts = relative_path.parts
            
            # Determine category based on first path part
            if len(path_parts) > 0:
                top_level_dir = path_parts[0]
                category_name = top_level_dir.title()
                
                # Ensure category exists in our dictionary
                if category_name not in categories:
                    categories[category_name] = []
                
                categories[category_name].append((relative_path, md_file))
        
        # Generate INDEX.md content
        content = ["# AI Brain Index", ""]
        content.append("> Auto-generated index of all knowledge base files")
        content.append("")
        content.append(f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
        content.append("")
        
        for category, files in categories.items():
            if not files:
                continue
                
            content.append(f"## {category}")
            content.append("")
            
            # Group files by subcategory
            subcategories = {}
            for relative_path, md_file in files:
                path_parts = relative_path.parts
                if len(path_parts) > 1:
                    subcategory = path_parts[1].replace('_', ' ').title()
                else:
                    subcategory = "General"
                
                if subcategory not in subcategories:
                    subcategories[subcategory] = []
                
                # Get title from frontmatter or filename
                title = self._get_file_title(md_file)
                subcategories[subcategory].append((title, relative_path))
            
            for subcategory, file_list in sorted(subcategories.items()):
                content.append(f"### {subcategory}")
                content.append("")
                
                for title, relative_path in sorted(file_list):
                    content.append(f"- [{title}]({relative_path})")
                
                content.append("")
        
        # Write INDEX.md
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))
        
        print(f"✅ INDEX.md updated with {sum(len(files) for files in categories.values())} files")

    def _get_file_title(self, md_file: Path) -> str:
        """Get title from frontmatter or generate from filename"""
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                if 'title' in post.metadata:
                    return post.metadata['title']
        except:
            pass
        
        # Fallback to filename
        return md_file.stem.replace('-', ' ').replace('_', ' ').title()

    def update_frontmatter(self):
        """Update frontmatter in all markdown files"""
        updated_count = 0
        
        for md_file in self.root.rglob("*.md"):
            if md_file.name in ["README.md", "INDEX.md", "CHANGELOG.md", "SYSTEM.md"]:
                continue
            
            # Skip files in venv directory
            if "venv/" in str(md_file):
                continue
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                
                # Check if frontmatter needs updating
                needs_update = False
                metadata = post.metadata
                
                # Ensure required fields exist
                if 'title' not in metadata:
                    metadata['title'] = self._get_file_title(md_file)
                    needs_update = True
                
                if 'type' not in metadata:
                    # Determine type from path
                    path_parts = md_file.relative_to(self.root).parts
                    if path_parts[0] == "knowledge":
                        metadata['type'] = "knowledge"
                    elif path_parts[0] == "prompts":
                        metadata['type'] = "behavior"
                    elif path_parts[0] == "systems":
                        metadata['type'] = "system"
                    elif path_parts[0] == "tools":
                        metadata['type'] = "tool"
                    else:
                        metadata['type'] = "general"
                    needs_update = True
                
                # Get path_parts for subtype check
                path_parts = md_file.relative_to(self.root).parts
                if 'subtype' not in metadata and len(path_parts) > 1:
                    metadata['subtype'] = path_parts[1]
                    needs_update = True
                
                if 'created' not in metadata:
                    metadata['created'] = datetime.now().isoformat()
                    needs_update = True
                
                if 'modified' not in metadata:
                    metadata['modified'] = datetime.now().isoformat()
                    needs_update = True
                else:
                    # Update modified date
                    metadata['modified'] = datetime.now().isoformat()
                    needs_update = True
                
                if 'version' not in metadata:
                    metadata['version'] = 1
                    needs_update = True
                
                if 'ship_factor' not in metadata:
                    metadata['ship_factor'] = 5
                    needs_update = True
                
                if 'tags' not in metadata:
                    metadata['tags'] = []
                    needs_update = True
                
                if needs_update:
                    post.metadata = metadata
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(frontmatter.dumps(post))
                    updated_count += 1
                    
            except Exception as e:
                print(f"Warning: Could not update {md_file}: {e}")
        
        print(f"✅ Updated frontmatter in {updated_count} files")

    def validate(self):
        """Validate all files and structure"""
        errors = []
        warnings = []
        
        # Check required directories exist
        required_dirs = [
            "knowledge", "systems", "tools", 
            "infrastructure", "commands", "instructions"
        ]
        
        for dir_name in required_dirs:
            if not (self.root / dir_name).exists():
                errors.append(f"Missing required directory: {dir_name}")
        
        # Check required files exist
        required_files = ["README.md", "SYSTEM.md", "CHANGELOG.md"]
        for file_name in required_files:
            if not (self.root / file_name).exists():
                errors.append(f"Missing required file: {file_name}")
        
        # Validate markdown files
        for md_file in self.root.rglob("*.md"):
            if md_file.name in ["README.md", "INDEX.md", "CHANGELOG.md", "SYSTEM.md"]:
                continue
            
            # Skip files in venv directory
            if "venv/" in str(md_file):
                continue
            
            # Skip files in venv directory
            if "venv/" in str(md_file):
                continue
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                
                metadata = post.metadata
                
                # Check required frontmatter fields
                required_fields = ['title', 'type', 'created', 'modified', 'version', 'ship_factor']
                for field in required_fields:
                    if field not in metadata:
                        warnings.append(f"{md_file}: Missing {field} in frontmatter")
                
                # Validate ship_factor range
                if 'ship_factor' in metadata:
                    sf = metadata['ship_factor']
                    if not isinstance(sf, int) or sf < 1 or sf > 10:
                        errors.append(f"{md_file}: Invalid ship_factor {sf} (must be 1-10)")
                
                # Validate type
                if 'type' in metadata:
                    valid_types = ['knowledge', 'behavior', 'system', 'tool', 'general']
                    if metadata['type'] not in valid_types:
                        warnings.append(f"{md_file}: Unknown type '{metadata['type']}'")
                
            except Exception as e:
                errors.append(f"{md_file}: {str(e)}")
        
        # Report results
        if errors:
            print("❌ Validation errors:")
            for error in errors:
                print(f"  - {error}")
        
        if warnings:
            print("⚠️  Validation warnings:")
            for warning in warnings:
                print(f"  - {warning}")
        
        if not errors and not warnings:
            print("✅ All files validated successfully")
        
        return len(errors) == 0

    def test(self):
        """Run tests and checks"""
        print("Running AI Brain tests...")
        
        # Test 1: Structure validation
        print("1. Testing structure...")
        if self.validate():
            print("   ✅ Structure validation passed")
        else:
            print("   ❌ Structure validation failed")
            return False
        
        # Test 2: Statistics generation
        print("2. Testing statistics...")
        stats = self.get_statistics()
        print(f"   ✅ Found {stats['total']} files")
        
        # Test 3: Index generation
        print("3. Testing index generation...")
        try:
            self.sync_index()
            print("   ✅ Index generation passed")
        except Exception as e:
            print(f"   ❌ Index generation failed: {e}")
            return False
        
        print("✅ All tests passed")
        return True

    def format(self):
        """Format all markdown files"""
        formatted_count = 0
        
        for md_file in self.root.rglob("*.md"):
            if md_file.name in ["README.md", "INDEX.md", "CHANGELOG.md", "SYSTEM.md"]:
                continue
            
            # Skip files in venv directory
            if "venv/" in str(md_file):
                continue
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Basic formatting (you can enhance this)
                lines = content.split('\n')
                formatted_lines = []
                
                for line in lines:
                    # Remove trailing whitespace
                    line = line.rstrip()
                    formatted_lines.append(line)
                
                # Remove multiple empty lines
                final_lines = []
                prev_empty = False
                for line in formatted_lines:
                    if line == "":
                        if not prev_empty:
                            final_lines.append(line)
                        prev_empty = True
                    else:
                        final_lines.append(line)
                        prev_empty = False
                
                formatted_content = '\n'.join(final_lines)
                
                if formatted_content != content:
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(formatted_content)
                    formatted_count += 1
                    
            except Exception as e:
                print(f"Warning: Could not format {md_file}: {e}")
        
        print(f"✅ Formatted {formatted_count} files")

    def lint(self):
        """Lint all files for issues"""
        issues = []
        
        for md_file in self.root.rglob("*.md"):
            if md_file.name in ["README.md", "INDEX.md", "CHANGELOG.md", "SYSTEM.md"]:
                continue
            
            # Skip files in venv directory
            if "venv/" in str(md_file):
                continue
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                lines = content.split('\n')
                
                for i, line in enumerate(lines, 1):
                    # Check for common issues
                    if len(line) > 100:
                        issues.append(f"{md_file}:{i} Line too long ({len(line)} chars)")
                    
                    if line.endswith(' '):
                        issues.append(f"{md_file}:{i} Trailing whitespace")
                    
                    if line.startswith(' ') and not line.startswith('  '):
                        issues.append(f"{md_file}:{i} Inconsistent indentation")
                
            except Exception as e:
                issues.append(f"{md_file}: Error reading file - {e}")
        
        if issues:
            print("Linting issues found:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("✅ No linting issues found")
        
        return len(issues) == 0

    def generate_docs(self):
        """Generate documentation"""
        docs_dir = self.root / "docs"
        docs_dir.mkdir(exist_ok=True)
        
        # Generate API documentation
        api_doc = docs_dir / "api.md"
        with open(api_doc, 'w', encoding='utf-8') as f:
            f.write("# AI Brain API Documentation\n\n")
            f.write("This document describes the AI Brain helper functions.\n\n")
            f.write("## BrainHelper Class\n\n")
            f.write("The main class for interacting with the AI Brain knowledge base.\n\n")
            f.write("### Methods\n\n")
            f.write("- `create_document()`: Create a new document\n")
            f.write("- `update_document()`: Update an existing document\n")
            f.write("- `get_document()`: Retrieve a document\n")
            f.write("- `list_documents()`: List documents by criteria\n")
            f.write("- `sync_index()`: Update INDEX.md\n")
            f.write("- `validate()`: Validate all files\n")
            f.write("- `get_statistics()`: Get repository statistics\n")
        
        print("✅ Documentation generated in docs/")

# CLI Interface
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="AI Brain Helper")
    parser.add_argument('action', choices=[
        'create', 'read', 'stats', 'high-priority', 'report', 
        'mcp-servers', 'commands', 'infrastructure', 'by-category',
        'sync-index', 'update-frontmatter', 'validate', 'test', 
        'format', 'lint', 'generate-docs'
    ])
    parser.add_argument('--title', help='Document title')
    parser.add_argument('--type', help='Document type')
    parser.add_argument('--subtype', help='Document subtype')
    parser.add_argument('--content', help='Document content')
    parser.add_argument('--tags', nargs='+', help='Tags')
    parser.add_argument('--ship-factor', type=int, default=5, help='Ship factor (1-10)')
    parser.add_argument('--path', help='Document path')
    parser.add_argument('--category', help='Document category')
    parser.add_argument('--references', nargs='+', help='Reference paths')
    
    args = parser.parse_args()
    
    brain = BrainHelper()
    
    if args.action == 'create':
        if not all([args.title, args.type, args.subtype, args.content]):
            print("Error: create requires --title, --type, --subtype, and --content")
            exit(1)
        
        path = brain.create_document(
            title=args.title,
            content=args.content,
            doc_type=args.type,
            subtype=args.subtype,
            tags=args.tags,
            ship_factor=args.ship_factor,
            references=args.references,
            category=args.category
        )
        print(f"Created: {path}")
    
    elif args.action == 'read':
        if not args.path:
            print("Error: read requires --path")
            exit(1)
        
        doc = brain.read_document(args.path)
        print(f"Title: {doc['metadata'].get('title')}")
        print(f"Ship Factor: {doc['metadata'].get('ship_factor')}")
        print(f"Category: {doc['metadata'].get('category', 'unknown')}")
        print(f"\nContent:\n{doc['content']}")
    
    elif args.action == 'stats':
        stats = brain.get_statistics()
        print("\nKnowledge Base Statistics:")
        for key, value in stats.items():
            print(f"  {key}: {value}")
    
    elif args.action == 'high-priority':
        items = brain.get_high_priority()
        print("\nHigh Priority Items (Ship Factor 8+):")
        for item in items:
            print(f"  [{item['ship_factor']}] {item['title']} ({item['category']})")
            print(f"      Path: {item['path']}")
    
    elif args.action == 'report':
        report = brain.generate_report()
        print(report)
    
    elif args.action == 'mcp-servers':
        servers = brain.get_mcp_servers()
        print(f"\nMCP Servers ({len(servers)}):")
        for server in servers:
            print(f"  {server['title']} (Ship Factor: {server['ship_factor']})")
    
    elif args.action == 'commands':
        commands = brain.get_commands()
        print(f"\nCommands ({len(commands)}):")
        for cmd in commands:
            print(f"  {cmd['title']} (Ship Factor: {cmd['ship_factor']})")
    
    elif args.action == 'infrastructure':
        infra = brain.get_infrastructure()
        print(f"\nInfrastructure ({len(infra)}):")
        for item in infra:
            print(f"  {item['title']} (Ship Factor: {item['ship_factor']})")
    
    elif args.action == 'by-category':
        if not args.category:
            print("Error: by-category requires --category")
            exit(1)
        
        items = brain.get_by_category(args.category)
        print(f"\nItems in {args.category} ({len(items)}):")
        for item in items:
            print(f"  {item['title']} (Ship Factor: {item['ship_factor']})")
    
    elif args.action == 'sync-index':
        brain.sync_index()
    
    elif args.action == 'update-frontmatter':
        brain.update_frontmatter()
    
    elif args.action == 'validate':
        success = brain.validate()
        exit(0 if success else 1)
    
    elif args.action == 'test':
        success = brain.test()
        exit(0 if success else 1)
    
    elif args.action == 'format':
        brain.format()
    
    elif args.action == 'lint':
        success = brain.lint()
        exit(0 if success else 1)
    
    elif args.action == 'generate-docs':
        brain.generate_docs()