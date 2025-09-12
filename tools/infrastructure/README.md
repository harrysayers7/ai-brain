# Infrastructure

Server and infrastructure configurations.

## Servers

### Production Server
```yaml
name: sayers-server
ip: 134.199.159.190
location: /servers/production.md
purpose: Main application server
access: SSH with key
```

## Structure

- `servers/` - Individual server configurations
- `docker/` - Docker and container configs
- `databases/` - Database connection info
- `networking/` - Network configurations

## Security Note

⚠️ This directory contains infrastructure references only.
- NO passwords
- NO private keys
- NO sensitive credentials

Use references like:
```yaml
ssh_key:
  location: ~/.ssh/id_rsa
  passphrase: STORED_IN_KEYCHAIN
```