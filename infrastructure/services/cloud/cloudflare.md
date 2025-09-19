---
created: '2025-01-27T00:00:00.000000'
modified: '2025-09-19T21:15:49.093987'
ship_factor: 6
subtype: cloud
tags:
- cloudflare
- cdn
- dns
title: Cloudflare Configuration
type: infrastructure
version: 1
---

# Cloudflare Configuration

## Account Information
```yaml
account_id: [TO_BE_DEFINED]
email: [TO_BE_DEFINED]
plan: [free|pro|business|enterprise]
```

## Zones (Domains)
```yaml
zones:
  - domain: [TO_BE_DEFINED]
    status: [active|pending]
    plan: [TO_BE_DEFINED]
    
  - domain: [TO_BE_DEFINED]
    status: [active|pending]
    plan: [TO_BE_DEFINED]
```

## DNS Records
```yaml
dns_records:
  - type: [A|AAAA|CNAME|MX|TXT]
    name: [TO_BE_DEFINED]
    content: [TO_BE_DEFINED]
    ttl: [auto|1|120|300|etc]
    proxied: [true|false]
```

## Security Features
```yaml
security:
  ssl_tls: [flexible|full|full_strict]
  always_use_https: [on|off]
  http_strict_transport_security: [on|off]
  min_tls_version: [1.0|1.1|1.2|1.3]
  
firewall_rules:
  - name: [TO_BE_DEFINED]
    action: [block|challenge|allow]
    expression: [TO_BE_DEFINED]
```

## Performance Features
```yaml
caching:
  level: [basic|simplified|aggressive]
  browser_cache_ttl: [TO_BE_DEFINED]
  
speed:
  mirage: [on|off]
  rocket_loader: [on|off]
  minify: [css|html|js]
  
compression:
  brotli: [on|off]
  gzip: [on|off]
```

## Workers & Functions
```yaml
workers:
  - name: [TO_BE_DEFINED]
    script: [TO_BE_DEFINED]
    routes: [TO_BE_DEFINED]
    
pages:
  - name: [TO_BE_DEFINED]
    domain: [TO_BE_DEFINED]
    build_command: [TO_BE_DEFINED]
```

## Access Information
```yaml
api_tokens:
  location: ~/.cloudflare/api_token
  permissions: [zone:read|zone:edit|account:read]
  
wrangler_cli:
  version: [TO_BE_DEFINED]
  login_status: [authenticated|not_authenticated]
```