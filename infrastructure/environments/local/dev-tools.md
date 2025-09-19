---
created: '2025-09-16T15:05:15.617786'
modified: '2025-09-19T21:15:49.107471'
ship_factor: 5
subtype: local
tags: []
title: Dev Tools
type: general
version: 1
---

# Development Tools

Tools and configurations for local development.

## Core Tools

### Package Managers
```bash
# macOS
brew install [packages]

# Node
npm install -g [packages]
pnpm install -g [packages]

# Python
pip install [packages]
```

### CLI Tools
```yaml
essential:
  - git
  - gh (GitHub CLI)
  - docker
  - kubectl
  - terraform
  
productivity:
  - tmux
  - fzf
  - ripgrep
  - jq
  - httpie
```

## IDE Extensions

### VS Code / Cursor
```yaml
essential:
  - GitHub Copilot
  - ESLint
  - Prettier
  - Docker
  
ai_assisted:
  - Continue
  - Codeium
  - [OTHER]
```

## Local Databases

### PostgreSQL
```yaml
version: 15
port: 5432
data: ~/postgres-data/
access: localhost
```

### Redis
```yaml
version: 7
port: 6379
config: ~/redis.conf
```

## Environment Setup

### Shell Config
```bash
# ~/.zshrc or ~/.bashrc
export PATH="$HOME/.local/bin:$PATH"
export EDITOR="code"

# Project aliases
alias brain="cd ~/Projects/ai-brain"
alias dev="cd ~/Projects"
```

### Git Config
```bash
git config --global user.name "[NAME]"
git config --global user.email "[EMAIL]"
git config --global init.defaultBranch main
```