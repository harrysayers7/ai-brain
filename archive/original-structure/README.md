# Local Development Environment

Local machine setup and configurations.

## Structure

- `workstation.md` - Main development machine specs
- `dev-tools.md` - Installed development tools
- `docker-compose.yml` - Local service stack
- `env-template.md` - Environment variables template

## Quick Setup

1. Check requirements in `workstation.md`
2. Install tools from `dev-tools.md`
3. Copy env template and configure
4. Run local stack with Docker Compose

## Security Note

⚠️ Never commit actual .env files
Use `.env.template` or `.env.example` only