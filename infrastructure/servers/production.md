---
created: '2025-09-16T15:05:15.620791'
modified: '2025-09-17T16:14:24.424819'
ship_factor: 5
subtype: servers
tags: []
title: Production
type: general
version: 1
---

# Production Server

## Server Details
```yaml
hostname: sayers-server
ip_address: 134.199.159.190
os: Ubuntu Linux (5.15.0-152-generic)
arch: x86_64
virtualization: KVM
provider: [PROVIDER_NAME]
```

## Hardware
```yaml
cpu:
  model: Intel DO-Premium-Intel
  cores: 4
  threads: 4
memory:
  total: 7.8 GB
storage:
  primary: 90 GB (vda)
  type: virtual
```

## Installed Software
```yaml
containerization:
  - Docker
  - Docker Compose
  
applications:
  location: /opt/
  installed:
    - erpnext
    - n8n
    - supabase

web_server:
  preferred: Caddy
  alternative: Nginx
```

## Access
```yaml
ssh:
  port: 22
  user: [USERNAME]
  auth: SSH key
  key_location: ~/.ssh/[KEY_NAME]

firewall:
  - 22/tcp (SSH)
  - 80/tcp (HTTP)
  - 443/tcp (HTTPS)
  - [OTHER_PORTS]
```

## Docker Services
```yaml
running_containers:
  - service: n8n
    port: 5678
    status: active
  
  - service: supabase
    port: 3000
    status: active
    
  - service: [OTHER_SERVICES]
```

## Maintenance
```yaml
backup:
  frequency: daily
  location: [BACKUP_LOCATION]
  
monitoring:
  - Disk usage
  - Memory usage
  - Service health
  
updates:
  schedule: weekly
  auto_security: enabled
```

## Notes

- Prefer Caddy over Nginx for reverse proxy
- All services containerized
- Regular backups configured
- Monitoring via [MONITORING_TOOL]