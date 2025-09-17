#!/bin/bash
# Setup script for automated documentation system
# This script sets up both context monitoring and SYSTEM.md auto-update

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Setting up Automated Documentation System${NC}"
echo -e "${BLUE}=========================================${NC}"
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
chmod +x scripts/system-md-updater.py
chmod +x scripts/git-hooks/post-commit-context
chmod +x scripts/git-hooks/post-commit-system-update
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
    # Create combined post-commit hook
    cat > .git/hooks/post-commit << 'EOF'
#!/bin/bash
# Combined post-commit hook for automated documentation

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Running automated documentation updates...${NC}"

# Get the repository root
REPO_ROOT=$(git rev-parse --show-toplevel)
cd "$REPO_ROOT"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run context monitoring
echo -e "${BLUE}Checking context file changes...${NC}"
if [ -f "scripts/context-monitor.py" ]; then
    python3 scripts/context-monitor.py
fi

# Run system update
echo -e "${BLUE}Updating SYSTEM.md...${NC}"
if [ -f "scripts/system-md-updater.py" ]; then
    python3 scripts/system-md-updater.py --update
fi

echo -e "${GREEN}✅ Automated documentation updates complete${NC}"
EOF
    
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

echo -e "${BLUE}Testing SYSTEM.md updater...${NC}"
source venv/bin/activate
python3 scripts/system-md-updater.py --update
echo -e "${GREEN}✅ SYSTEM.md updater test passed${NC}"

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
echo "  make update-system      # Update SYSTEM.md based on codebase"
echo "  make analyze-codebase   # Generate detailed analysis report"
echo "  make update            # Run full update cycle (includes all automation)"
echo ""
echo -e "${GREEN}Automatic Features:${NC}"
echo "  - Context file changes are automatically documented"
echo "  - SYSTEM.md is automatically updated on structural changes"
echo "  - All changes are tracked in CHANGELOG.md"
echo "  - Notifications are sent for important changes"
echo ""
echo -e "${GREEN}Configuration Files:${NC}"
echo "  .context-monitor-state.json     # Context file state tracking"
echo "  .context-notifier-config.json  # Notification configuration"
echo "  codebase-analysis-report.md    # Detailed analysis report"
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

# Check SYSTEM.md
echo -e "${BLUE}Documentation:${NC}"
if [ -f "SYSTEM.md" ]; then
    echo -e "  ✅ SYSTEM.md (auto-updated)"
else
    echo -e "  ❌ SYSTEM.md (missing)"
fi

if [ -f "codebase-analysis-report.md" ]; then
    echo -e "  ✅ codebase-analysis-report.md"
else
    echo -e "  ⚠️  codebase-analysis-report.md (run 'make analyze-codebase' to generate)"
fi
echo ""

echo -e "${GREEN}🎉 Automated documentation system setup complete!${NC}"
echo ""
echo -e "${YELLOW}Next Steps:${NC}"
echo "1. The system will automatically update documentation on commits"
echo "2. Run 'make analyze-codebase' to generate detailed analysis"
echo "3. Configure notifications if desired"
echo "4. The system maintains SYSTEM.md context as the codebase evolves"
echo ""
echo -e "${BLUE}For help, run: make help${NC}"
