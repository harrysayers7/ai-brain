#!/usr/bin/env python3
"""
AI Brain Helper Utilities

Utility functions for managing the AI Brain knowledge base.
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
        """Ensure all required directories exist"""
        directories = [
            "knowledge/decisions",
            "knowledge/lessons",
            "knowledge/references",
            "behaviors/personas",
            "behaviors/modes",
            "systems/workflows",
            "systems/rules",
            "tools/integrations"
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
        references: List[str] = None
    ) -> str:
        """Create a new document with frontmatter"""
        
        # Generate filename from title
        slug = self._slugify(title)
        path = self.root / doc_type / subtype / f"{slug}.md"
        
        # Check if file exists
        if path.exists():
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
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
            if md_file.name in ['SYSTEM.md', 'INDEX.md', 'README.md']:
                continue
            
            with open(md_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            doc_tags = post.get('tags', [])
            if any(tag in doc_tags for tag in tags):
                results.append({
                    'path': str(md_file.relative_to(self.root)),
                    'title': post.get('title', 'Untitled'),
                    'tags': doc_tags,
                    'ship_factor': post.get('ship_factor', 0)
                })
        
        return sorted(results, key=lambda x: x['ship_factor'], reverse=True)
    
    def get_high_priority(self, min_ship_factor: int = 8) -> List[Dict]:
        """Get all high-priority items"""
        results = []
        
        for md_file in self.root.rglob("*.md"):
            if md_file.name in ['SYSTEM.md', 'INDEX.md', 'README.md']:
                continue
            
            with open(md_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            if post.get('ship_factor', 0) >= min_ship_factor:
                if not post.get('deprecated', False):
                    results.append({
                        'path': str(md_file.relative_to(self.root)),
                        'title': post.get('title', 'Untitled'),
                        'ship_factor': post.get('ship_factor'),
                        'modified': post.get('modified')
                    })
        
        return sorted(results, key=lambda x: x['ship_factor'], reverse=True)
    
    def update_index(self):
        """Update the INDEX.md file with current content"""
        # This is a simplified version - extend as needed
        stats = self.get_statistics()
        high_priority = self.get_high_priority()
        
        # Read current INDEX.md and update statistics section
        # (Implementation depends on your specific needs)
        print(f"Index updated: {stats['total']} total items")
    
    def get_statistics(self) -> Dict[str, int]:
        """Get statistics about the knowledge base"""
        stats = {
            'total': 0,
            'decisions': 0,
            'lessons': 0,
            'workflows': 0,
            'deprecated': 0
        }
        
        for md_file in self.root.rglob("*.md"):
            if md_file.name in ['SYSTEM.md', 'INDEX.md', 'README.md']:
                continue
            
            stats['total'] += 1
            
            with open(md_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            if post.get('deprecated', False):
                stats['deprecated'] += 1
            
            subtype = post.get('subtype', '')
            if 'decision' in subtype:
                stats['decisions'] += 1
            elif 'lesson' in subtype:
                stats['lessons'] += 1
            elif 'workflow' in subtype:
                stats['workflows'] += 1
        
        return stats
    
    def _slugify(self, text: str) -> str:
        """Convert text to URL-friendly slug"""
        import re
        text = text.lower()
        text = re.sub(r'[^a-z0-9]+', '-', text)
        text = text.strip('-')
        return text


# CLI Interface
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="AI Brain Helper")
    parser.add_argument('action', choices=['create', 'read', 'stats', 'high-priority'])
    parser.add_argument('--title', help='Document title')
    parser.add_argument('--type', help='Document type')
    parser.add_argument('--subtype', help='Document subtype')
    parser.add_argument('--content', help='Document content')
    parser.add_argument('--tags', nargs='+', help='Tags')
    parser.add_argument('--ship-factor', type=int, default=5, help='Ship factor (1-10)')
    parser.add_argument('--path', help='Document path')
    
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
            ship_factor=args.ship_factor
        )
        print(f"Created: {path}")
    
    elif args.action == 'read':
        if not args.path:
            print("Error: read requires --path")
            exit(1)
        
        doc = brain.read_document(args.path)
        print(f"Title: {doc['metadata'].get('title')}")
        print(f"Ship Factor: {doc['metadata'].get('ship_factor')}")
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
            print(f"  [{item['ship_factor']}] {item['title']}")
            print(f"      Path: {item['path']}")