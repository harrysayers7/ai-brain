---
created: '2025-09-19T06:58:56.082902'
modified: '2025-09-19T06:58:56.082907'
ship_factor: 5
subtype: context
tags: []
title: Infrastructure
type: general
version: 1
---

# Infrastructure Context

This file provides a high-level overview of the AI Brain infrastructure setup. Detailed configurations are stored in the `infrastructure/` directory.

## Production Server

**Primary Server**: `sayers-server` (134.199.159.190)
- **OS**: Ubuntu Linux
- **Resources**: 4 CPU cores, 7.8GB RAM, 90GB storage
- **Virtualization**: KVM
- **Access**: SSH with key authentication

## Running Services

### Containerized Applications
- **n8n**: Workflow automation (Port 5678)
- **Supabase**: Database and backend services (Port 3000)
- **Other services**: Additional containerized applications

### Web Server
- **Preferred**: Caddy (reverse proxy)
- **Alternative**: Nginx
- **Ports**: 80 (HTTP), 443 (HTTPS), 22 (SSH)

## Database

- **Primary**: Supabase
- **Type**: PostgreSQL-based
- **Location**: Containerized on production server
- **Access**: Via Supabase dashboard and API

## Infrastructure Structure

```
infrastructure/
├── .DS_Store    # Configuration file
├── README.md    # Documentation
├── databases/                   # Database configurations
├── docker/                   # Docker configurations
├── local/                   # Local machine setup and configurations.
├── networking/                   # Network configurations
├── servers/                   # Server configurations
```

## Security

- SSH key authentication only
- No passwords stored in repository
- Firewall configured for essential ports only
- Regular security updates enabled

## Monitoring

- Disk usage monitoring
- Memory usage tracking
- Service health checks
- Daily backups configured

## Maintenance

- **Updates**: Weekly scheduled updates
- **Backups**: Daily automated backups
- **Monitoring**: Continuous service health monitoring
- **Access**: SSH with key-based authentication

*Note: This context file is automatically synchronized with the infrastructure directory.*