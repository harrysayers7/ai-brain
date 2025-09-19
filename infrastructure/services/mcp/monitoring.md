---
created: '2025-01-27T00:00:00.000000'
modified: '2025-01-27T00:00:00.000000'
ship_factor: 6
subtype: monitoring
tags: [mcp, monitoring, observability, ai]
title: MCP Servers Monitoring
type: infrastructure
version: 1
---

# MCP Servers Monitoring

Monitoring and observability configuration for MCP (Model Context Protocol) servers.

## Health Checks
```yaml
health_endpoints:
  filesystem-mcp:
    url: http://localhost:3001/health
    interval: 30s
    timeout: 5s
    expected_status: 200
    expected_response: {"status": "healthy"}
    
  github-mcp:
    url: http://localhost:3002/health
    interval: 30s
    timeout: 5s
    expected_status: 200
    expected_response: {"status": "healthy"}
    
  database-mcp:
    url: http://localhost:3003/health
    interval: 30s
    timeout: 5s
    expected_status: 200
    expected_response: {"status": "healthy"}
    
  web-mcp:
    url: http://localhost:3004/health
    interval: 30s
    timeout: 5s
    expected_status: 200
    expected_response: {"status": "healthy"}
```

## Metrics Collection
```yaml
prometheus_metrics:
  enabled: true
  port: 9090
  scrape_interval: 30s
  
  targets:
    - name: filesystem-mcp
      endpoint: http://filesystem-mcp:3000/metrics
      
    - name: github-mcp
      endpoint: http://github-mcp:3000/metrics
      
    - name: database-mcp
      endpoint: http://database-mcp:3000/metrics
      
    - name: web-mcp
      endpoint: http://web-mcp:3000/metrics

custom_metrics:
  - name: mcp_requests_total
    type: counter
    description: Total number of MCP requests
    
  - name: mcp_request_duration_seconds
    type: histogram
    description: MCP request duration
    
  - name: mcp_active_connections
    type: gauge
    description: Active MCP connections
    
  - name: mcp_error_rate
    type: gauge
    description: MCP error rate percentage
```

## Logging Configuration
```yaml
log_collection:
  level: info
  format: json
  output: stdout
  
  structured_fields:
    - timestamp
    - level
    - service
    - request_id
    - user_id
    - operation
    - duration
    - status_code
    
  log_aggregation:
    method: [elasticsearch|loki|fluentd]
    endpoint: [TO_BE_DEFINED]
    index_pattern: mcp-logs-*
    
  retention:
    period: 30 days
    compression: gzip
    rotation: daily
```

## Alerting Rules
```yaml
alerts:
  - name: MCP_Server_Down
    condition: up{job="mcp-*"} == 0
    duration: 1m
    severity: critical
    description: MCP server is down
    
  - name: MCP_High_Error_Rate
    condition: rate(mcp_errors_total[5m]) > 0.1
    duration: 2m
    severity: warning
    description: High error rate on MCP server
    
  - name: MCP_High_Response_Time
    condition: histogram_quantile(0.95, rate(mcp_request_duration_seconds_bucket[5m])) > 5
    duration: 3m
    severity: warning
    description: High response time on MCP server
    
  - name: MCP_Memory_High
    condition: container_memory_usage_bytes / container_spec_memory_limit_bytes > 0.8
    duration: 5m
    severity: warning
    description: High memory usage on MCP server
    
  - name: MCP_CPU_High
    condition: rate(container_cpu_usage_seconds_total[5m]) > 0.8
    duration: 5m
    severity: warning
    description: High CPU usage on MCP server
```

## Dashboard Configuration
```yaml
grafana_dashboards:
  - name: MCP Servers Overview
    panels:
      - title: Server Status
        type: stat
        query: up{job=~"mcp-.*"}
        
      - title: Request Rate
        type: graph
        query: rate(mcp_requests_total[5m])
        
      - title: Response Time
        type: graph
        query: histogram_quantile(0.95, rate(mcp_request_duration_seconds_bucket[5m]))
        
      - title: Error Rate
        type: graph
        query: rate(mcp_errors_total[5m])
        
      - title: Active Connections
        type: graph
        query: mcp_active_connections
        
      - title: Memory Usage
        type: graph
        query: container_memory_usage_bytes / container_spec_memory_limit_bytes
        
      - title: CPU Usage
        type: graph
        query: rate(container_cpu_usage_seconds_total[5m])

  - name: MCP Server Details
    panels:
      - title: Request Distribution by Server
        type: pie
        query: sum(rate(mcp_requests_total[5m])) by (server)
        
      - title: Top Operations
        type: table
        query: topk(10, sum(rate(mcp_requests_total[5m])) by (operation))
        
      - title: Error Distribution
        type: graph
        query: sum(rate(mcp_errors_total[5m])) by (server, error_type)
```

## Performance Monitoring
```yaml
performance_metrics:
  - name: request_throughput
    description: Requests per second
    calculation: rate(mcp_requests_total[1m])
    threshold: [TO_BE_DEFINED]
    
  - name: response_time_p95
    description: 95th percentile response time
    calculation: histogram_quantile(0.95, rate(mcp_request_duration_seconds_bucket[5m]))
    threshold: [TO_BE_DEFINED]
    
  - name: error_rate
    description: Error rate percentage
    calculation: rate(mcp_errors_total[5m]) / rate(mcp_requests_total[5m]) * 100
    threshold: [TO_BE_DEFINED]
    
  - name: connection_pool_utilization
    description: Connection pool utilization
    calculation: mcp_active_connections / mcp_max_connections * 100
    threshold: [TO_BE_DEFINED]
```

## Security Monitoring
```yaml
security_monitoring:
  - name: failed_authentication_attempts
    query: rate(mcp_auth_failures_total[5m])
    threshold: [TO_BE_DEFINED]
    action: alert
    
  - name: suspicious_request_patterns
    query: rate(mcp_requests_total{operation=~".*sensitive.*"}[5m])
    threshold: [TO_BE_DEFINED]
    action: alert
    
  - name: rate_limit_violations
    query: rate(mcp_rate_limit_violations_total[5m])
    threshold: [TO_BE_DEFINED]
    action: alert
```

## Notification Channels
```yaml
notifications:
  - name: slack-alerts
    type: slack
    webhook_url: STORED_IN_ENV_VARS
    channel: "#mcp-alerts"
    severity: [critical|warning]
    
  - name: email-alerts
    type: email
    smtp_server: [TO_BE_DEFINED]
    recipients: [TO_BE_DEFINED]
    severity: [critical]
    
  - name: pagerduty
    type: pagerduty
    integration_key: STORED_IN_ENV_VARS
    severity: [critical]
    
  - name: webhook
    type: webhook
    url: [TO_BE_DEFINED]
    severity: [critical|warning|info]
```

## Backup and Recovery Monitoring
```yaml
backup_monitoring:
  - name: backup_success
    query: mcp_backup_success_total
    expected_frequency: daily
    
  - name: backup_duration
    query: mcp_backup_duration_seconds
    threshold: [TO_BE_DEFINED]
    
  - name: backup_size
    query: mcp_backup_size_bytes
    threshold: [TO_BE_DEFINED]

recovery_monitoring:
  - name: recovery_time
    query: mcp_recovery_duration_seconds
    threshold: [TO_BE_DEFINED]
    
  - name: data_loss
    query: mcp_data_loss_bytes
    threshold: 0
```

## Compliance and Audit
```yaml
audit_logging:
  enabled: true
  
  events:
    - authentication
    - authorization
    - data_access
    - configuration_changes
    - admin_actions
    
  retention:
    period: 7 years
    format: immutable
    
  compliance:
    - gdpr
    - sox
    - hipaa
    - [TO_BE_DEFINED]
```
