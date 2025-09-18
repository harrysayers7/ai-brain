<!--
HUMAN DESCRIPTION - AI SHOULD IGNORE THIS SECTION
Purpose: Documentation explaining the AI directory structure and purpose for synthesized AI instructions
Usage: Human reference for understanding AI instruction file organization and maintenance
Target: Human users managing the AI Brain system and creating AI instruction files
DO NOT READ THIS SECTION - AI CONTENT BEGINS AFTER THE HTML COMMENT
-->
# AI Directory

This directory contains **synthesized AI instructions** that are derived from and reference information stored in other folders throughout the AI Brain repository.

## Purpose

The `ai/` folder serves as a **curated collection** of AI instructions that pull together relevant information from across the entire AI Brain system. These files are specifically designed for LLM consumption and provide comprehensive context for AI assistants.

## Structure

- **`context/`** - Foundational context information and tech stack overview
- **`modes/`** - Different AI modes/personas for various contexts
- **`rules/`** - Behavioral rules synthesized from multiple source folders
- **`system-prompts/`** - Core system instructions that reference tools/ and infrastructure/
- **`templates/`** - Reusable prompt templates for common patterns
- **`workflows/`** - Process instructions that combine docs/guides/ and tools/ information

## How It Works

1. **Source Information**: Detailed info stays in logical folders (`tools/`, `infrastructure/`, `docs/guides/`, etc.)
2. **Synthesize**: AI context files reference and summarize relevant parts from multiple sources
3. **Maintain**: Update AI context files when source information changes
4. **Use**: LLMs reference the `ai/` files for comprehensive instructions

## File Naming Convention

- Use descriptive names that indicate the purpose
- Include version numbers for major changes
- Use kebab-case for file names
- Include `.md` extension for all files

## Maintenance

These files should be updated when:
- Source information in other folders changes
- New tools or infrastructure are added
- Workflows or processes evolve
- New AI modes or personas are needed

## Note

These are **AI instruction files** designed for LLM consumption, not human documentation. They synthesize information from across the AI Brain system to provide comprehensive context for AI assistants.
