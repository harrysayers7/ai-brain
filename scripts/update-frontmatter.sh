#!/bin/bash
# Update frontmatter in all markdown files
# This script is called by the Makefile and git hooks

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Updating frontmatter...${NC}"

# Run the Python helper to update frontmatter
python3 utils/brain_helper.py update-frontmatter

echo -e "${GREEN}✅ Frontmatter updated${NC}"
