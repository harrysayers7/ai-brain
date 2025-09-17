## Basic Operations

| Command           | Description                        |
|-------------------|------------------------------------|
| `make git-status` | Show git status                    |
| `make git-add`    | Add all changes                    |
| `make git-commit` | Commit with message prompt         |
| `make git-save`   | Quick save (add + auto-commit)     |

## AI Brain Specific

| Command               | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `make git-save-ai`    | Save with AI Brain message                                                  |
| `make git-commit-ai`  | Commit with AI Brain message (includes validation & context monitoring)      |

## Sync Operations

| Command         | Description         |
|-----------------|---------------------|
| `make git-push` | Push to remote      |
| `make git-pull` | Pull from remote    |
| `make git-sync` | Pull then push      |

## Information

| Command           | Description             |
|-------------------|------------------------|
| `make git-log`    | Show recent commits    |
| `make git-diff`   | Show staged changes    |
| `make git-branch` | Show current branch    |

## Maintenance

| Command               | Description                |
|-----------------------|---------------------------|
| `make git-stash`      | Stash changes             |
| `make git-clean`      | Clean untracked files     |
| `make git-reset-soft` | Soft reset last commit    |

---

## Key Features

- **AI Brain Integration:**  
  The `git-commit-ai` command runs pre-commit validation and context monitoring.

- **Color-coded Output:**  
  Easy to read with colored status messages.

- **Safety Features:**  
  Confirmation prompts for destructive operations.

- **Comprehensive Help:**  
  `make git-help` shows all available commands.

- **Flexible Operations:**  
  Support for different types of commits and operations.