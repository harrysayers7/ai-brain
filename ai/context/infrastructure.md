---
created: '2025-09-19T06:58:56.082902'
modified: '2025-09-19T21:15:49.311138'
ship_factor: 5
subtype: context
tags: []
title: Infrastructure
type: general
version: 2
---

# Infrastructure Context

This file provides a high-level overview of the AI Brain infrastructure setup. Detailed configurations are stored in the `infrastructure/` directory.

## Production Server

**Primary Server**: `sayers-server` (134.199.159.190)
- **OS**: Ubuntu Linux
- **Resources**: 4 CPU cores, 7.8GB RAM, 90GB storage
- **Virtualization**: KVM
- **Access**: SSH with key authentication

## Database

- **Primary**: Supabase
- **Type**: PostgreSQL-based
- **Location**: Containerized on production server
- **Access**: Via Supabase dashboard and API

## Infrastructure Structure

```
infrastructure/
├── .DS_Store    # Configuration file
├── INFRASTRUCTURE-OVERVIEW.md    # Documentation
├── README.md    # Documentation
├── containers/                   # containers configurations
├── databases/                   # Database configurations
├── docker/                   # Docker configurations
├── environments/                   # environments configurations
├── local/                   # Local development tools
├── networking/                   # Network configurations
├── security/                   # security configurations
├── servers/                   # Server configurations
├── services/                   # services configurations
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