#!/bin/bash
# Setup script for context file monitoring automation
# This script sets up the complete automation system for tracking context file updates

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Setting up Context File Monitoring Automation${NC}"
echo -e "${BLUE}==============================================${NC}"
echo ""

# Get repository root
REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
cd "$REPO_ROOT"

echo -e "${BLUE}Repository root: $REPO_ROOT${NC}"
echo ""

# 1. Make scripts executable
echo -e "${YELLOW}1. Making scripts executable...${NC}"
chmod +x scripts/context-monitor.py
chmod +x scripts/context-notifier.py
chmod +x scripts/git-hooks/post-commit-context
echo -e "${GREEN}✅ Scripts made executable${NC}"
echo ""

# 2. Install Python dependencies
echo -e "${YELLOW}2. Installing Python dependencies...${NC}"
if [ -d "venv" ]; then
    echo -e "${BLUE}Using existing virtual environment...${NC}"
    source venv/bin/activate
    pip install python-frontmatter pyyaml requests
    echo -e "${GREEN}✅ Dependencies installed in virtual environment${NC}"
else
    echo -e "${BLUE}Creating virtual environment...${NC}"
    python3 -m venv venv
    source venv/bin/activate
    pip install python-frontmatter pyyaml requests
    echo -e "${GREEN}✅ Virtual environment created and dependencies installed${NC}"
fi
echo ""

# 3. Initialize context monitoring state
echo -e "${YELLOW}3. Initializing context monitoring state...${NC}"
source venv/bin/activate
python3 scripts/context-monitor.py --force-update
echo -e "${GREEN}✅ Context monitoring state initialized${NC}"
echo ""

# 4. Setup git hooks
echo -e "${YELLOW}4. Setting up git hooks...${NC}"
if [ -d ".git/hooks" ]; then
    # Copy post-commit hook
    cp scripts/git-hooks/post-commit-context .git/hooks/post-commit
    chmod +x .git/hooks/post-commit
    echo -e "${GREEN}✅ Git hooks configured${NC}"
else
    echo -e "${RED}❌ Not a git repository - skipping git hooks${NC}"
fi
echo ""

# 5. Test the system
echo -e "${YELLOW}5. Testing the system...${NC}"
echo -e "${BLUE}Running context monitor test...${NC}"
source venv/bin/activate
python3 scripts/context-monitor.py
echo -e "${GREEN}✅ Context monitor test passed${NC}"

echo -e "${BLUE}Testing notification system...${NC}"
source venv/bin/activate
python3 scripts/context-notifier.py --test
echo -e "${GREEN}✅ Notification system test passed${NC}"
echo ""

# 6. Show usage instructions
echo -e "${YELLOW}6. Usage Instructions${NC}"
echo -e "${BLUE}===================${NC}"
echo ""
echo -e "${GREEN}Manual Commands:${NC}"
echo "  make monitor-context    # Check for context file changes"
echo "  make watch-context      # Watch context files continuously"
echo "  make update            # Run full update cycle (includes context monitoring)"
echo ""
echo -e "${GREEN}Notification Setup:${NC}"
echo "  python3 scripts/context-notifier.py --setup-email    # Setup email notifications"
echo "  python3 scripts/context-notifier.py --setup-webhook  # Setup webhook notifications"
echo "  python3 scripts/context-notifier.py --enable console # Enable console notifications"
echo "  python3 scripts/context-notifier.py --disable file   # Disable file logging"
echo ""
echo -e "${GREEN}Configuration Files:${NC}"
echo "  .context-monitor-state.json     # Context file state tracking"
echo "  .context-notifier-config.json  # Notification configuration"
echo "  context-updates.log            # Update log file"
echo "  CONTEXT-UPDATE-SUMMARY.md      # Latest update summary"
echo ""

# 7. Show current status
echo -e "${YELLOW}7. Current Status${NC}"
echo -e "${BLUE}================${NC}"
echo ""

# Check if context files exist
echo -e "${BLUE}Context Files:${NC}"
for file in "ai/context/infrastructure.md" "ai/context/tech-stack.md"; do
    if [ -f "$file" ]; then
        echo -e "  ✅ $file"
    else
        echo -e "  ❌ $file (missing)"
    fi
done
echo ""

# Check configuration files
echo -e "${BLUE}Configuration Files:${NC}"
for file in ".context-monitor-state.json" ".context-notifier-config.json"; do
    if [ -f "$file" ]; then
        echo -e "  ✅ $file"
    else
        echo -e "  ⚠️  $file (will be created on first run)"
    fi
done
echo ""

# Check git hooks
echo -e "${BLUE}Git Hooks:${NC}"
if [ -f ".git/hooks/post-commit" ]; then
    echo -e "  ✅ post-commit hook installed"
else
    echo -e "  ❌ post-commit hook not installed"
fi
echo ""

echo -e "${GREEN}🎉 Context file monitoring automation setup complete!${NC}"
echo ""
echo -e "${YELLOW}Next Steps:${NC}"
echo "1. Update your context files to test the system"
echo "2. Configure notifications if desired"
echo "3. The system will automatically track changes and update documentation"
echo ""
echo -e "${BLUE}For help, run: make help${NC}"
