#!/bin/bash

# AI Brain Setup Script
# Installs dependencies and configures the maintenance system

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Setting up AI Brain maintenance system...${NC}"

# Check if we're in the right directory
if [ ! -f "utils/brain_helper.py" ]; then
    echo -e "${RED}❌ Please run this script from the ai-brain root directory${NC}"
    exit 1
fi

# Install Python dependencies
echo -e "${YELLOW}Installing Python dependencies...${NC}"
if command -v pip3 &> /dev/null; then
    pip3 install python-frontmatter pyyaml
    echo -e "${GREEN}✅ Dependencies installed${NC}"
else
    echo -e "${RED}❌ pip3 not found. Please install Python dependencies manually:${NC}"
    echo "  pip3 install python-frontmatter pyyaml"
    exit 1
fi

# Make scripts executable
echo -e "${YELLOW}Making scripts executable...${NC}"
chmod +x scripts/*.sh
chmod +x .git/hooks/*
echo -e "${GREEN}✅ Scripts made executable${NC}"

# Test the system
echo -e "${YELLOW}Testing the system...${NC}"
if python3 utils/brain_helper.py test; then
    echo -e "${GREEN}✅ System test passed${NC}"
else
    echo -e "${YELLOW}⚠️  System test had issues, but setup continues${NC}"
fi

# Run initial update
echo -e "${YELLOW}Running initial update...${NC}"
python3 utils/brain_helper.py sync-index
python3 utils/brain_helper.py update-frontmatter

echo -e "${GREEN}✅ AI Brain maintenance system setup complete!${NC}"
echo ""
echo -e "${BLUE}Available commands:${NC}"
echo "  make help          # Show all available commands"
echo "  make update        # Run full update cycle"
echo "  make validate      # Validate all files"
echo "  make test          # Run tests"
echo "  make stats         # Show repository statistics"
echo ""
echo -e "${BLUE}Git integration:${NC}"
echo "  - Pre-commit hook: Validates files before commit"
echo "  - Post-commit hook: Updates files after commit"
echo ""
echo -e "${BLUE}Manual maintenance:${NC}"
echo "  python3 utils/brain_helper.py sync-index"
echo "  python3 utils/brain_helper.py update-frontmatter"
echo "  python3 utils/brain_helper.py validate"
