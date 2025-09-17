# Git Operations Makefile
# Convenient git commands for AI Brain project

.PHONY: git-status git-add git-commit git-push git-pull git-log git-diff git-stash git-clean git-reset git-validate-repo

# Validate we're in the AI Brain repository
git-validate-repo:
	@if [ ! -d ".git" ]; then \
		echo "$(RED)❌ Not in a git repository$(NC)"; \
		exit 1; \
	fi
	@if [ "$$(git remote get-url origin 2>/dev/null | grep -o 'ai-brain.git')" != "ai-brain.git" ]; then \
		echo "$(RED)❌ Not in the AI Brain repository$(NC)"; \
		echo "$(YELLOW)Current repository: $$(git remote get-url origin 2>/dev/null || echo 'No origin remote')$(NC)"; \
		exit 1; \
	fi

# Git status
git-status: git-validate-repo ## Show git status
	@echo "$(BLUE)Git Status$(NC)"
	@echo "$(BLUE)==========$(NC)"
	@git status --short

# Git add operations
git-add: git-validate-repo ## Add all changes to staging
	@echo "$(BLUE)Adding all changes...$(NC)"
	@git add .
	@echo "$(GREEN)✅ All changes added to staging$(NC)"

git-add-modified: git-validate-repo ## Add only modified files
	@echo "$(BLUE)Adding modified files...$(NC)"
	@git add -u
	@echo "$(GREEN)✅ Modified files added to staging$(NC)"

git-add-new: git-validate-repo ## Add only new files
	@echo "$(BLUE)Adding new files...$(NC)"
	@git add -A
	@echo "$(GREEN)✅ New files added to staging$(NC)"

# Git commit operations
git-commit: git-validate-repo ## Commit staged changes (requires message)
	@echo "$(BLUE)Committing changes...$(NC)"
	@read -p "Enter commit message: " msg; \
	git commit -m "$$msg"
	@echo "$(GREEN)✅ Changes committed$(NC)"

git-commit-auto: git-validate-repo ## Auto-commit with timestamp
	@echo "$(BLUE)Auto-committing changes...$(NC)"
	@git commit -m "Update: $(shell date '+%Y-%m-%d %H:%M:%S')"
	@echo "$(GREEN)✅ Changes auto-committed$(NC)"

git-commit-ai: git-validate-repo ## Commit with AI Brain update message
	@echo "$(BLUE)Committing AI Brain updates...$(NC)"
	@git commit -m "AI Brain: Update documentation and context files"
	@echo "$(GREEN)✅ AI Brain updates committed$(NC)"

# Combined operations
git-save: git-validate-repo git-add git-commit-auto ## Quick save: add all and commit with timestamp
	@echo "$(GREEN)✅ Quick save complete$(NC)"

git-save-ai: git-validate-repo git-add git-commit-ai ## AI Brain save: add all and commit with AI message
	@echo "$(GREEN)✅ AI Brain save complete$(NC)"

# Git push/pull operations
git-push: git-validate-repo ## Push changes to remote
	@echo "$(BLUE)Pushing changes...$(NC)"
	@git push
	@echo "$(GREEN)✅ Changes pushed$(NC)"

git-pull: git-validate-repo ## Pull changes from remote
	@echo "$(BLUE)Pulling changes...$(NC)"
	@git pull
	@echo "$(GREEN)✅ Changes pulled$(NC)"

git-sync: git-validate-repo git-pull git-push ## Sync: pull then push
	@echo "$(GREEN)✅ Repository synced$(NC)"

# Git information
git-log: git-validate-repo ## Show recent commit log
	@echo "$(BLUE)Recent Commits$(NC)"
	@echo "$(BLUE)==============$(NC)"
	@git log --oneline -10

git-diff: git-validate-repo ## Show staged changes
	@echo "$(BLUE)Staged Changes$(NC)"
	@echo "$(BLUE)==============$(NC)"
	@git diff --cached

git-diff-unstaged: git-validate-repo ## Show unstaged changes
	@echo "$(BLUE)Unstaged Changes$(NC)"
	@echo "$(BLUE)================$(NC)"
	@git diff

# Git maintenance
git-stash: git-validate-repo ## Stash current changes
	@echo "$(BLUE)Stashing changes...$(NC)"
	@git stash push -m "Stash: $(shell date '+%Y-%m-%d %H:%M:%S')"
	@echo "$(GREEN)✅ Changes stashed$(NC)"

git-stash-pop: git-validate-repo ## Pop latest stash
	@echo "$(BLUE)Popping stash...$(NC)"
	@git stash pop
	@echo "$(GREEN)✅ Stash popped$(NC)"

git-clean: git-validate-repo ## Clean untracked files (use with caution)
	@echo "$(RED)⚠️  This will remove untracked files$(NC)"
	@read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ]
	@git clean -fd
	@echo "$(GREEN)✅ Untracked files cleaned$(NC)"

git-reset-soft: git-validate-repo ## Soft reset last commit (keeps changes staged)
	@echo "$(YELLOW)Soft resetting last commit...$(NC)"
	@git reset --soft HEAD~1
	@echo "$(GREEN)✅ Last commit reset (changes staged)$(NC)"

git-reset-hard: git-validate-repo ## Hard reset last commit (loses changes)
	@echo "$(RED)⚠️  This will lose all uncommitted changes$(NC)"
	@read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ]
	@git reset --hard HEAD~1
	@echo "$(GREEN)✅ Last commit reset (changes lost)$(NC)"

# Git branch operations
git-branch: git-validate-repo ## Show current branch
	@echo "$(BLUE)Current Branch$(NC)"
	@echo "$(BLUE)==============$(NC)"
	@git branch --show-current

git-branches: git-validate-repo ## List all branches
	@echo "$(BLUE)All Branches$(NC)"
	@echo "$(BLUE)============$(NC)"
	@git branch -a

git-new-branch: git-validate-repo ## Create new branch
	@echo "$(BLUE)Creating new branch...$(NC)"
	@read -p "Enter branch name: " branch; \
	git checkout -b "$$branch"
	@echo "$(GREEN)✅ New branch created and checked out$(NC)"

# Git help
git-help: ## Show git help
	@echo "$(BLUE)AI Brain Git Operations Help$(NC)"
	@echo "$(BLUE)============================$(NC)"
	@echo ""
	@echo "$(GREEN)⚠️  These commands only work in the AI Brain repository!$(NC)"
	@echo ""
	@echo "$(YELLOW)Basic Operations:$(NC)"
	@echo "  make git-status     # Show git status"
	@echo "  make git-add        # Add all changes"
	@echo "  make git-commit     # Commit with message prompt"
	@echo "  make git-save       # Quick save (add + auto-commit)"
	@echo ""
	@echo "$(YELLOW)AI Brain Specific:$(NC)"
	@echo "  make git-save-ai    # Save with AI Brain message"
	@echo "  make git-commit-ai  # Commit with AI Brain message"
	@echo ""
	@echo "$(YELLOW)Sync Operations:$(NC)"
	@echo "  make git-push       # Push to remote"
	@echo "  make git-pull       # Pull from remote"
	@echo "  make git-sync       # Pull then push"
	@echo ""
	@echo "$(YELLOW)Information:$(NC)"
	@echo "  make git-log        # Show recent commits"
	@echo "  make git-diff       # Show staged changes"
	@echo "  make git-branch     # Show current branch"
	@echo ""
	@echo "$(YELLOW)Maintenance:$(NC)"
	@echo "  make git-stash      # Stash changes"
	@echo "  make git-clean      # Clean untracked files"
	@echo "  make git-reset-soft # Soft reset last commit"
	@echo ""
	@echo "$(YELLOW)Repository Validation:$(NC)"
	@echo "  All commands validate you're in the AI Brain repository"
	@echo "  before executing to prevent accidental operations"

# Colors for output
RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[1;33m
BLUE := \033[0;34m
NC := \033[0m # No Color
