#!/bin/bash
# Update INDEX.md with current file structure
# This script is called by the Makefile and git hooks

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Updating INDEX.md...${NC}"

# Run the Python helper to sync index
python3 utils/brain_helper.py sync-index

echo -e "${GREEN}✅ INDEX.md updated${NC}"




