---
created: '2025-01-27T00:00:00.000000'
modified: '2025-09-19T21:15:49.089147'
ship_factor: 7
subtype: mcp
tags:
- mcp
- servers
- infrastructure
- ai
title: MCP Servers Configuration
type: infrastructure
version: 1
---

# MCP Servers Configuration

Model Context Protocol (MCP) servers provide AI assistants with access to external systems and data sources.

## Server Inventory
```yaml
mcp_servers:
  - name: filesystem-fastmcp
    port: 3001
    environment: production
    purpose: File system access and operations
    status: running
    server: 134.199.159.190
    access_method: ssh_tunnel_required

  - name: upbank
    port: 3002
    environment: production
    purpose: Up Bank transaction tracking and account management
    status: running
    server: 134.199.159.190
    access_method: ssh_tunnel_required
    api_status: authenticated_and_working
```

## Local Development Servers
```yaml
local_servers:
  - name: filesystem-mcp
    port: 3001
    purpose: File system access and operations
    docker_image: [TO_BE_DEFINED]
    environment_vars:
      - MCP_FS_ROOT: [TO_BE_DEFINED]
      - MCP_FS_PERMISSIONS: [TO_BE_DEFINED]
    
  - name: github-mcp
    port: 3002
    purpose: GitHub API integration
    docker_image: [TO_BE_DEFINED]
    environment_vars:
      - GITHUB_TOKEN: STORED_IN_ENV_VARS
      - GITHUB_OWNER: [TO_BE_DEFINED]
      
  - name: database-mcp
    port: 3003
    purpose: Database operations
    docker_image: [TO_BE_DEFINED]
    environment_vars:
      - DB_CONNECTION_STRING: STORED_IN_ENV_VARS
      - DB_TYPE: [postgresql|mysql|sqlite]
      
  - name: web-mcp
    port: 3004
    purpose: Web scraping and HTTP operations
    docker_image: [TO_BE_DEFINED]
    environment_vars:
      - WEB_PROXY: [TO_BE_DEFINED]
      - USER_AGENT: [TO_BE_DEFINED]
```

## Production Servers
```yaml
production_servers:
  - name: [TO_BE_DEFINED]
    port: [TO_BE_DEFINED]
    purpose: [TO_BE_DEFINED]
    docker_image: [TO_BE_DEFINED]
    replicas: [TO_BE_DEFINED]
    resources:
      cpu: [TO_BE_DEFINED]
      memory: [TO_BE_DEFINED]
    health_check:
      endpoint: [TO_BE_DEFINED]
      interval: [TO_BE_DEFINED]
```

## Configuration Management
```yaml
config_files:
  - name: mcp-config.json
    location: ~/.mcp.json
    purpose: Global MCP configuration
    
  - name: server-configs
    location: [TO_BE_DEFINED]
    purpose: Individual server configurations

environment_variables:
  - MCP_SERVER_PORT: [TO_BE_DEFINED]
  - MCP_SERVER_HOST: [TO_BE_DEFINED]
  - MCP_LOG_LEVEL: [debug|info|warn|error]
  - MCP_AUTH_TOKEN: STORED_IN_ENV_VARS
```

## Network Configuration
```yaml
ports:
  - port: 3001
    service: filesystem-mcp
    protocol: HTTP
    access: localhost
    
  - port: 3002
    service: github-mcp
    protocol: HTTP
    access: localhost
    
  - port: 3003
    service: database-mcp
    protocol: HTTP
    access: localhost
    
  - port: 3004
    service: web-mcp
    protocol: HTTP
    access: localhost

firewall_rules:
  - port: [TO_BE_DEFINED]
    source: [TO_BE_DEFINED]
    action: [allow|deny]
```

## Security Configuration
```yaml
authentication:
  type: [token|oauth|api_key]
  token_location: STORED_IN_ENV_VARS
  token_rotation: [30|60|90] days
  
access_control:
  allowed_hosts: [localhost|TO_BE_DEFINED]
  rate_limiting: [enabled|disabled]
  max_requests_per_minute: [TO_BE_DEFINED]
  
ssl_tls:
  enabled: [true|false]
  certificate: [TO_BE_DEFINED]
  key: [TO_BE_DEFINED]
```

## Monitoring and Logging
```yaml
monitoring:
  health_checks:
    - endpoint: /health
      interval: [30] seconds
      timeout: [5] seconds
      
  metrics:
    - endpoint: /metrics
      format: [prometheus|json]
      collection_interval: [60] seconds
    
logging:
  level: [debug|info|warn|error]
  format: [json|text]
  output: [stdout|file|syslog]
  file_location: [TO_BE_DEFINED]
  retention: [7|30|90] days
```

## Deployment
```yaml
deployment_method: [docker|kubernetes|systemd|manual]

docker:
  compose_file: docker-compose.mcp.yml
  registry: [TO_BE_DEFINED]
  tag: [latest|TO_BE_DEFINED]
  
kubernetes:
  namespace: [TO_BE_DEFINED]
  deployment_file: [TO_BE_DEFINED]
  service_file: [TO_BE_DEFINED]
  
systemd:
  service_files:
    - [TO_BE_DEFINED]
```

## Backup and Recovery
```yaml
backup:
  configuration_files: [true|false]
  server_data: [true|false]
  frequency: [daily|weekly|monthly]
  location: [TO_BE_DEFINED]
  
recovery:
  procedure: [TO_BE_DEFINED]
  rto: [TO_BE_DEFINED] minutes
  rpo: [TO_BE_DEFINED] minutes
```

## Server-Specific Documentation

### upbank MCP Server

**Purpose**: Up Bank transaction tracking and account management via their API

**Port**: 8002
**Server**: 134.199.159.190
**Status**: ✅ Running

**Available Tools**:
- `list_accounts` - Get all Up Bank accounts with balances
- `get_account_balance` - Get balance for specific account
- `list_transactions` - List recent transactions with filtering
- `get_transaction` - Get detailed transaction information
- `list_categories` - Get spending categories
- `search_transactions` - Search transactions by various criteria
- `service_status` - Get server status and configuration

**Configuration**:
- API Base URL: https://api.up.com.au/api/v1
- Authentication: Bearer token (configured via UPBANK_API_TOKEN)
- Rate Limit: 1000 requests per hour
- Data Directory: `/opt/mcp-data/upbank`

**Claude Desktop Integration**:
```json
"upbank": {
  "command": "npx",
  "args": ["@modelcontextprotocol/server-sse-client", "http://localhost:8002/sse"]
}
```

### filesystem-fastmcp MCP Server

**Purpose**: File system access and operations

**Port**: 8001
**Server**: 134.199.159.190
**Status**: ✅ Running

**Claude Desktop Integration**:
```json
"filesystem-fastmcp": {
  "command": "npx",
  "args": ["@modelcontextprotocol/server-sse-client", "http://localhost:8001/sse"]
}
```

## 🌐 **24/7 Access Options**

### **SSH Tunnel Access (Secure)**
```bash
ssh -L 8001:localhost:8001 -L 8002:localhost:8002 root@134.199.159.190
# Then access: http://localhost:8001/sse and http://localhost:8002/sse
```

### **Direct Access (Configured)**
- **Status**: Server configured for public access
- **Firewall**: Ports 8001, 8002 opened
- **Network**: Docker containers bound to 0.0.0.0
- **Issue**: External access may be blocked by hosting provider firewall

**Current Public Endpoints** (DigitalOcean Cloud Firewall blocks external access):
- Filesystem: `http://134.199.159.190:3001/sse`
- Upbank: `http://134.199.159.190:3002/sse`

**Status**:
- ✅ Server configured for public access (0.0.0.0 binding)
- ✅ UFW firewall rules added for ports 3001, 3002
- ❌ DigitalOcean Cloud Firewall blocking external connections
- ✅ SSH tunnel working as reliable alternative

### **Claude Desktop Config Options**

**Option 1: SSH Tunnel (Recommended - Works Now)**
```json
{
  "mcpServers": {
    "filesystem-fastmcp": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-sse-client", "http://localhost:3001/sse"]
    },
    "upbank": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-sse-client", "http://localhost:3002/sse"]
    }
  }
}
```
*Requires SSH tunnel: `ssh -L 3001:localhost:3001 -L 3002:localhost:3002 root@134.199.159.190`*

**Option 2: Direct Access (After Adding DigitalOcean Firewall Rules)**
```json
{
  "mcpServers": {
    "filesystem-fastmcp": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-sse-client", "http://134.199.159.190:3001/sse"]
    },
    "upbank": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-sse-client", "http://134.199.159.190:3002/sse"]
    }
  }
}
```

### **To Enable Direct Access**
Add inbound rules in DigitalOcean Control Panel → Networking → Firewalls:
- **Port 3001**: TCP, Source: All IPv4 + All IPv6
- **Port 3002**: TCP, Source: All IPv4 + All IPv6

## Integration Points
```yaml
ai_clients:
  - name: claude-desktop
    config_location: ~/Library/Application Support/Claude/claude_desktop_config.json
    enabled_servers: [filesystem-fastmcp, upbank]

  - name: cursor
    config_location: ~/.cursor/mcp.json
    enabled_servers: [TO_BE_DEFINED]

  - name: [TO_BE_DEFINED]
    config_location: [TO_BE_DEFINED]
    enabled_servers: [TO_BE_DEFINED]
```