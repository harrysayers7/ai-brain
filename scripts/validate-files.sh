#!/bin/bash
# Validate all files and structure
# This script is called by the Makefile and git hooks

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Validating AI Brain structure...${NC}"

# Run the Python helper to validate
python3 utils/brain_helper.py validate

echo -e "${GREEN}✅ Validation complete${NC}"




