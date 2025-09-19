---
created: '2025-01-27T00:00:00.000000'
modified: '2025-01-27T00:00:00.000000'
ship_factor: 8
subtype: security
tags: [ssh, keys, security, access]
title: SSH Keys Configuration
type: infrastructure
version: 1
---

# SSH Keys Configuration

## Available SSH Keys
```yaml
keys:
  - name: [TO_BE_DEFINED]
    location: ~/.ssh/[KEY_NAME]
    type: [ed25519|rsa|ecdsa]
    size: [256|2048|4096|521]
    purpose: [personal|work|server|deployment]
    passphrase: [STORED_IN_KEYCHAIN|none]
    
  - name: [TO_BE_DEFINED]
    location: ~/.ssh/[KEY_NAME]
    type: [ed25519|rsa|ecdsa]
    size: [256|2048|4096|521]
    purpose: [personal|work|server|deployment]
    passphrase: [STORED_IN_KEYCHAIN|none]
```

## Key Usage
```yaml
server_access:
  production_server:
    key: [KEY_NAME]
    user: [USERNAME]
    host: [HOSTNAME_OR_IP]
    
  development_server:
    key: [KEY_NAME]
    user: [USERNAME]
    host: [HOSTNAME_OR_IP]
    
  staging_server:
    key: [KEY_NAME]
    user: [USERNAME]
    host: [HOSTNAME_OR_IP]

git_access:
  github:
    key: [KEY_NAME]
    user: [USERNAME]
    
  gitlab:
    key: [KEY_NAME]
    user: [USERNAME]
```

## SSH Configuration
```yaml
config_file: ~/.ssh/config

hosts:
  - host: [HOSTNAME]
    hostname: [IP_OR_DOMAIN]
    user: [USERNAME]
    identityfile: ~/.ssh/[KEY_NAME]
    port: [22|CUSTOM_PORT]
    
  - host: [HOSTNAME]
    hostname: [IP_OR_DOMAIN]
    user: [USERNAME]
    identityfile: ~/.ssh/[KEY_NAME]
    port: [22|CUSTOM_PORT]
```

## Security Best Practices
```yaml
key_rotation:
  frequency: [6|12] months
  last_rotated: [DATE]
  next_rotation: [DATE]
  
access_control:
  key_permissions: 600
  config_permissions: 644
  directory_permissions: 700
  
backup:
  encrypted_backup: [true|false]
  backup_location: [TO_BE_DEFINED]
  recovery_plan: [TO_BE_DEFINED]
```

## Key Management
```yaml
ssh_agent:
  enabled: [true|false]
  keys_loaded: [KEY_LIST]
  timeout: [3600] seconds
  
key_generation:
  default_type: ed25519
  default_size: [256|4096]
  comment_format: "[USERNAME]@[HOSTNAME]"
```

## Emergency Access
```yaml
recovery_keys:
  - name: [TO_BE_DEFINED]
    location: [SECURE_LOCATION]
    purpose: emergency_access
    last_used: [DATE]
    
backup_access:
  method: [TO_BE_DEFINED]
  contact: [TO_BE_DEFINED]
  escalation: [TO_BE_DEFINED]
```
