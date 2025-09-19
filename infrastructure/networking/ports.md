---
created: '2025-01-27T00:00:00.000000'
modified: '2025-09-19T21:15:49.080713'
ship_factor: 6
subtype: networking
tags:
- ports
- networking
- services
title: Network Ports Configuration
type: infrastructure
version: 1
---

# Network Ports Configuration

## Standard Ports
```yaml
web_services:
  - port: 80
    service: HTTP
    protocol: TCP
    status: [open|closed|filtered]
    
  - port: 443
    service: HTTPS
    protocol: TCP
    status: [open|closed|filtered]
    
  - port: 8080
    service: HTTP_ALT
    protocol: TCP
    status: [open|closed|filtered]

ssh_access:
  - port: 22
    service: SSH
    protocol: TCP
    status: [open|closed|filtered]
    authentication: [key_based|password|both]

database_services:
  - port: 5432
    service: PostgreSQL
    protocol: TCP
    status: [open|closed|filtered]
    access: [local|remote|restricted]
    
  - port: 6379
    service: Redis
    protocol: TCP
    status: [open|closed|filtered]
    access: [local|remote|restricted]
    
  - port: 3306
    service: MySQL
    protocol: TCP
    status: [open|closed|filtered]
    access: [local|remote|restricted]
```

## Development Ports
```yaml
development:
  - port: 3000
    service: Frontend Dev Server
    protocol: TCP
    environment: [local|development]
    
  - port: 5000
    service: API Dev Server
    protocol: TCP
    environment: [local|development]
    
  - port: 8000
    service: Python Dev Server
    protocol: TCP
    environment: [local|development]
    
  - port: 9229
    service: Node.js Debug
    protocol: TCP
    environment: [local|development]
```

## Custom Application Ports
```yaml
applications:
  - port: [TO_BE_DEFINED]
    service: [TO_BE_DEFINED]
    protocol: [TCP|UDP]
    environment: [local|development|staging|production]
    
  - port: [TO_BE_DEFINED]
    service: [TO_BE_DEFINED]
    protocol: [TCP|UDP]
    environment: [local|development|staging|production]
```

## Firewall Configuration
```yaml
firewall_rules:
  inbound:
    - port: [TO_BE_DEFINED]
      source: [TO_BE_DEFINED]
      action: [allow|deny]
      protocol: [TCP|UDP|ALL]
      
  outbound:
    - port: [TO_BE_DEFINED]
      destination: [TO_BE_DEFINED]
      action: [allow|deny]
      protocol: [TCP|UDP|ALL]

iptables_rules:
  - rule: [TO_BE_DEFINED]
    chain: [INPUT|OUTPUT|FORWARD]
    target: [ACCEPT|DROP|REJECT]
```

## Port Security
```yaml
security_measures:
  port_scanning_protection: [enabled|disabled]
  rate_limiting: [enabled|disabled]
  fail2ban: [enabled|disabled]
  
monitoring:
  port_usage_monitoring: [enabled|disabled]
  connection_tracking: [enabled|disabled]
  anomaly_detection: [enabled|disabled]
```

## Load Balancer Configuration
```yaml
load_balancer:
  frontend_ports:
    - port: 80
      backend_ports: [3000, 3001]
      health_check: [enabled|disabled]
      
    - port: 443
      backend_ports: [3000, 3001]
      health_check: [enabled|disabled]
      ssl_termination: [enabled|disabled]
```

## VPN and Remote Access
```yaml
vpn_access:
  - port: 1194
    service: OpenVPN
    protocol: UDP
    access: [restricted|open]
    
  - port: 1723
    service: PPTP
    protocol: TCP
    access: [restricted|open]
    
  - port: 500
    service: IPSec
    protocol: UDP
    access: [restricted|open]
```