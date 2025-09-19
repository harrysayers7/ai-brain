# AI Brain Maintenance Makefile
# Automated maintenance and update system for the AI Brain knowledge base

# Include git operations
include $(dir $(lastword $(MAKEFILE_LIST)))git.mk

.PHONY: help install update validate test clean sync-index update-frontmatter check-deps format lint docs monitor-context watch-context update-system analyze-codebase integrated-update quick-update sync-context infra-scan infra-validate infra-backup infra-deploy infra-status infra-monitor

# Default target
.DEFAULT_GOAL := help

# Configuration
PYTHON := python3
BRAIN_HELPER := utils/brain_helper.py
CONTEXT_MONITOR := scripts/context-monitor.py
SYSTEM_UPDATER := scripts/system-md-updater.py
INTEGRATED_UPDATER := scripts/integrated-updater.py
CONTEXT_SYNC := scripts/context-sync.py
INFRASTRUCTURE_SCANNER := scripts/infrastructure-scanner.py
CHANGELOG := CHANGELOG.md
INDEX_FILE := INDEX.md
SYSTEM_FILE := SYSTEM.md
INFRASTRUCTURE_OVERVIEW := infrastructure/INFRASTRUCTURE-OVERVIEW.md

# Colors for output
RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[1;33m
BLUE := \033[0;34m
NC := \033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)AI Brain Maintenance System$(NC)"
	@echo "$(BLUE)============================$(NC)"
	@echo ""
	@echo "$(YELLOW)Available commands:$(NC)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)Quick start:$(NC)"
	@echo "  make install    # Install dependencies and setup"
	@echo "  make update     # Run full update cycle"
	@echo "  make validate   # Check all files for issues"

install: ## Install dependencies and setup git hooks
	@echo "$(BLUE)Installing AI Brain maintenance system...$(NC)"
	@pip3 install python-frontmatter pyyaml
	@chmod +x scripts/*.sh
	@chmod +x .git/hooks/*
	@echo "$(GREEN)✅ Dependencies installed and hooks configured$(NC)"

update: check-deps integrated-update ## Run complete update cycle (integrated)
	@echo "$(GREEN)✅ AI Brain update complete$(NC)"

integrated-update: ## Run integrated update cycle (efficient coordination)
	@echo "$(BLUE)Running integrated update cycle...$(NC)"
	@$(PYTHON) $(INTEGRATED_UPDATER) --full
	@echo "$(GREEN)✅ Integrated update complete$(NC)"

quick-update: ## Run quick update for recent changes
	@echo "$(BLUE)Running quick update...$(NC)"
	@$(PYTHON) $(INTEGRATED_UPDATER) --quick
	@echo "$(GREEN)✅ Quick update complete$(NC)"

sync-index: ## Update INDEX.md with current file structure
	@echo "$(BLUE)Syncing INDEX.md...$(NC)"
	@$(PYTHON) $(BRAIN_HELPER) sync-index
	@echo "$(GREEN)✅ INDEX.md updated$(NC)"

update-frontmatter: ## Update frontmatter in all markdown files
	@echo "$(BLUE)Updating frontmatter...$(NC)"
	@$(PYTHON) $(BRAIN_HELPER) update-frontmatter
	@echo "$(GREEN)✅ Frontmatter updated$(NC)"

validate: check-deps ## Validate all files and structure
	@echo "$(BLUE)Validating AI Brain structure...$(NC)"
	@$(PYTHON) $(BRAIN_HELPER) validate
	@echo "$(GREEN)✅ Validation complete$(NC)"

test: ## Run tests and checks
	@echo "$(BLUE)Running tests...$(NC)"
	@$(PYTHON) $(BRAIN_HELPER) test
	@echo "$(GREEN)✅ Tests passed$(NC)"

format: ## Format all markdown files
	@echo "$(BLUE)Formatting files...$(NC)"
	@$(PYTHON) $(BRAIN_HELPER) format
	@echo "$(GREEN)✅ Files formatted$(NC)"

lint: ## Lint all files for issues
	@echo "$(BLUE)Linting files...$(NC)"
	@$(PYTHON) $(BRAIN_HELPER) lint
	@echo "$(GREEN)✅ Linting complete$(NC)"

docs: ## Generate documentation
	@echo "$(BLUE)Generating documentation...$(NC)"
	@$(PYTHON) $(BRAIN_HELPER) generate-docs
	@echo "$(GREEN)✅ Documentation generated$(NC)"

monitor-context: ## Check for context file changes and update changelog
	@echo "$(BLUE)Monitoring context files...$(NC)"
	@$(PYTHON) $(CONTEXT_MONITOR)
	@echo "$(GREEN)✅ Context monitoring complete$(NC)"

watch-context: ## Watch context files for changes (continuous monitoring)
	@echo "$(BLUE)Starting context file watcher...$(NC)"
	@$(PYTHON) $(CONTEXT_MONITOR) --watch

update-system: ## Update SYSTEM.md based on current codebase state
	@echo "$(BLUE)Updating SYSTEM.md...$(NC)"
	@$(PYTHON) $(SYSTEM_UPDATER) --update
	@echo "$(GREEN)✅ SYSTEM.md updated$(NC)"

analyze-codebase: ## Generate detailed codebase analysis report
	@echo "$(BLUE)Analyzing codebase...$(NC)"
	@$(PYTHON) $(SYSTEM_UPDATER) --analyze
	@echo "$(GREEN)✅ Codebase analysis complete$(NC)"

sync-context: ## Synchronize context files with their source directories
	@echo "$(BLUE)Synchronizing context files...$(NC)"
	@$(PYTHON) $(CONTEXT_SYNC) --sync
	@echo "$(GREEN)✅ Context synchronization complete$(NC)"

check-deps: ## Check if dependencies are installed
	@echo "$(BLUE)Checking dependencies...$(NC)"
	@$(PYTHON) -c "import frontmatter, yaml" 2>/dev/null || (echo "$(RED)❌ Missing dependencies. Run 'make install'$(NC)" && exit 1)
	@echo "$(GREEN)✅ Dependencies OK$(NC)"

clean: ## Clean temporary files
	@echo "$(BLUE)Cleaning temporary files...$(NC)"
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -name ".DS_Store" -delete
	@echo "$(GREEN)✅ Cleanup complete$(NC)"

# Git integration targets
pre-commit: validate format lint ## Run pre-commit checks
	@echo "$(GREEN)✅ Pre-commit checks passed$(NC)"

post-commit: monitor-context update ## Run post-commit updates
	@echo "$(GREEN)✅ Post-commit updates complete$(NC)"

# Maintenance targets
backup: ## Create backup of current state
	@echo "$(BLUE)Creating backup...$(NC)"
	@mkdir -p backups
	@tar -czf backups/ai-brain-$(shell date +%Y%m%d-%H%M%S).tar.gz --exclude='.git' --exclude='backups' .
	@echo "$(GREEN)✅ Backup created$(NC)"

stats: ## Show repository statistics
	@echo "$(BLUE)AI Brain Statistics$(NC)"
	@echo "$(BLUE)==================$(NC)"
	@echo "Total markdown files: $$(find . -name '*.md' | wc -l)"
	@echo "Knowledge files: $$(find knowledge/ -name '*.md' 2>/dev/null | wc -l)"
	@echo "Tool files: $$(find tools/ -name '*.md' 2>/dev/null | wc -l)"
	@echo "System files: $$(find systems/ -name '*.md' 2>/dev/null | wc -l)"
	@echo "Prompt files: $$(find prompts/ -name '*.md' 2>/dev/null | wc -l)"
	@echo "High priority items: $$(grep -r 'ship_factor: [89]\|ship_factor: 10' --include='*.md' . | wc -l)"
	@echo "Deprecated items: $$(grep -r 'deprecated: true' --include='*.md' . | wc -l)"

# Development targets
dev-setup: install ## Setup development environment
	@echo "$(BLUE)Setting up development environment...$(NC)"
	@mkdir -p scripts
	@echo "$(GREEN)✅ Development environment ready$(NC)"

watch: ## Watch for changes and auto-update
	@echo "$(BLUE)Watching for changes...$(NC)"
	@while inotifywait -e modify,create,delete -r . --exclude '\.git'; do \
		echo "$(YELLOW)Change detected, running update...$(NC)"; \
		make update; \
	done

# Infrastructure targets
infra-scan: ## Scan infrastructure and update overview
	@echo "$(BLUE)Scanning infrastructure...$(NC)"
	@$(PYTHON) $(INFRASTRUCTURE_SCANNER) --scan
	@echo "$(GREEN)✅ Infrastructure overview updated$(NC)"

infra-validate: ## Validate infrastructure configuration
	@echo "$(BLUE)Validating infrastructure configuration...$(NC)"
	@$(PYTHON) $(INFRASTRUCTURE_SCANNER) --report
	@echo "$(GREEN)✅ Infrastructure validation complete$(NC)"

infra-backup: ## Backup infrastructure configurations
	@echo "$(BLUE)Creating infrastructure backup...$(NC)"
	@mkdir -p backups/infrastructure
	@tar -czf backups/infrastructure/infrastructure-$(shell date +%Y%m%d-%H%M%S).tar.gz infrastructure/
	@echo "$(GREEN)✅ Infrastructure backup created$(NC)"

infra-deploy: ## Deploy infrastructure changes
	@echo "$(BLUE)Deploying infrastructure changes...$(NC)"
	@echo "$(YELLOW)Note: This is a placeholder for actual deployment$(NC)"
	@echo "$(GREEN)✅ Infrastructure deployment complete$(NC)"

infra-status: ## Show infrastructure status
	@echo "$(BLUE)Infrastructure Status$(NC)"
	@echo "$(BLUE)==================$(NC)"
	@if [ -f "$(INFRASTRUCTURE_OVERVIEW)" ]; then \
		echo "Overview file: ✅ Present"; \
		echo "Last updated: $$(grep 'Last Updated' $(INFRASTRUCTURE_OVERVIEW) | head -1)"; \
	else \
		echo "Overview file: ❌ Missing"; \
	fi
	@echo "Total environments: $$(find infrastructure/environments -type d -maxdepth 1 | wc -l)"
	@echo "Total services: $$(find infrastructure/services -type d -maxdepth 1 | wc -l)"
	@echo "Total config files: $$(find infrastructure -name '*.md' | wc -l)"

infra-monitor: ## Monitor infrastructure health
	@echo "$(BLUE)Monitoring infrastructure health...$(NC)"
	@echo "$(YELLOW)Note: This is a placeholder for actual monitoring$(NC)"
	@echo "$(GREEN)✅ Infrastructure monitoring complete$(NC)"

# Emergency targets
emergency-reset: ## Reset to last known good state (use with caution)
	@echo "$(RED)⚠️  Emergency reset - this will reset to last commit$(NC)"
	@read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ]
	@git reset --hard HEAD
	@echo "$(GREEN)✅ Reset complete$(NC)"

# Help for specific targets
help-update:
	@echo "$(BLUE)Update System Help$(NC)"
	@echo "$(BLUE)==================$(NC)"
	@echo "The update system automatically:"
	@echo "1. Syncs INDEX.md with current file structure"
	@echo "2. Updates frontmatter in all markdown files"
	@echo "3. Validates file structure and content"
	@echo "4. Updates changelog (via git hooks)"
	@echo ""
	@echo "Run 'make update' to perform all updates manually"
	@echo "Updates run automatically on git commit"

help-git:
	@echo "$(BLUE)Git Integration Help$(NC)"
	@echo "$(BLUE)====================$(NC)"
	@echo "Git hooks are automatically configured:"
	@echo "- pre-commit: Validates files before commit"
	@echo "- post-commit: Updates files after commit"
	@echo ""
	@echo "Manual triggers:"
	@echo "- make pre-commit: Run pre-commit checks"
	@echo "- make post-commit: Run post-commit updates"




