# Integrations

Configurations for external tools, APIs, and services.

## What Belongs Here

- API endpoint configurations
- Webhook setups
- Third-party service settings
- Integration mappings
- Tool-specific configurations
- Environment-specific settings

## Integration Template

```markdown
---
title: [Integration] Service Name
type: tool
subtype: integration
tags: [service-name, api, category]
created: 2024-01-15T10:00:00Z
modified: 2024-01-15T10:00:00Z
version: 1
ship_factor: 8
active: true
environment: production
cost: $X/month
criticality: high|medium|low
---

# [Integration] Service Name

## Service Details

### Overview
- **Purpose**: What we use it for
- **Category**: API|Database|Monitoring|Analytics|etc
- **Vendor**: Company name
- **Contract**: [end date, terms]

### Environments

| Environment | Endpoint | Status | Notes |
|------------|----------|--------|-------|
| Production | api.service.com | Active | Primary |
| Staging | staging-api.service.com | Active | Testing |
| Development | sandbox.service.com | Active | Free tier |

## Authentication

### Method
- Type: API Key|OAuth2|JWT|Basic Auth
- Rotation: Frequency and process
- Permissions: Scope and limitations

### Credential Storage
```yaml
production:
  location: AWS_SECRETS_MANAGER
  path: /prod/service-name/credentials
  
staging:
  location: HASHICORP_VAULT
  path: /staging/service-name/credentials
  
development:
  location: ENV_VARIABLES
  variables:
    - SERVICE_API_KEY
    - SERVICE_SECRET
```

## Configuration

### Required Settings
```json
{
  "api_version": "v2",
  "timeout": 30,
  "retry_attempts": 3,
  "rate_limit": "100/minute",
  "webhook_url": "https://our-app.com/webhooks/service"
}
```

### Optional Features
- Feature 1: [enabled/disabled] - reason
- Feature 2: [enabled/disabled] - reason

## API Endpoints

| Operation | Method | Endpoint | Rate Limit |
|-----------|--------|----------|------------|
| List | GET | /api/v2/resources | 100/min |
| Create | POST | /api/v2/resources | 50/min |
| Update | PUT | /api/v2/resources/:id | 50/min |
| Delete | DELETE | /api/v2/resources/:id | 20/min |

## Webhooks

### Incoming
| Event | Endpoint | Handler |
|-------|----------|----------|
| resource.created | /webhooks/created | handleCreated() |
| resource.updated | /webhooks/updated | handleUpdated() |

### Outgoing
| Trigger | Target | Payload |
|---------|--------|----------|
| user.signup | service.com/hook | User object |
| order.complete | service.com/hook | Order object |

## Error Handling

### Common Errors

| Error Code | Meaning | Response |
|------------|---------|----------|
| 401 | Invalid credentials | Rotate key |
| 429 | Rate limited | Backoff + retry |
| 500 | Service error | Alert + fallback |
| 503 | Maintenance | Use cache |

### Retry Strategy
```python
retry_delays = [1, 2, 4, 8, 16]  # seconds
max_retries = 5
retry_on = [429, 502, 503, 504]
```

## Monitoring

### Health Checks
- Endpoint: `GET /health`
- Frequency: Every 60 seconds
- Timeout: 5 seconds
- Alert threshold: 3 failures

### Key Metrics
- API response time: < 500ms p95
- Error rate: < 1%
- Availability: > 99.9%
- Usage: X% of quota

### Dashboards
- [Internal Dashboard](link)
- [Vendor Status Page](link)
- [Datadog Monitor](link)

## Dependencies

### Our Systems That Use This
- System A: Critical path
- System B: Nice to have
- System C: Batch processing

### This Depends On
- Network connectivity
- DNS resolution
- SSL certificates

## Costs

### Pricing Model
- Base: $X/month
- Overage: $Y per 1000 requests
- Current usage: Z%
- Projected monthly: $total

### Optimization Opportunities
- [ ] Batch requests to reduce calls
- [ ] Cache responses for 5 minutes
- [ ] Move to annual plan for discount

## Migration/Upgrade Path

### Version Roadmap
- Current: v2 (until 2024-12-31)
- Next: v3 (available 2024-06-01)
- Migration deadline: 2024-12-31

### Migration Steps
1. Test in development
2. Update staging
3. Canary in production
4. Full rollout

## Disaster Recovery

### Backup Service
- Primary: This service
- Fallback: Alternative service
- Cache: 24-hour local cache
- Manual: CSV export process

### Outage Procedure
1. Detect via monitoring
2. Check vendor status page
3. Switch to fallback if > 5 min
4. Notify stakeholders
5. Document incident

## Contacts

### Internal
- Owner: Team/Person
- Technical: Developer
- Business: Product Manager

### Vendor
- Support: support@service.com
- Account Manager: name@service.com
- Emergency: +1-XXX-XXX-XXXX

## Documentation

- [API Documentation](link)
- [Integration Guide](link)
- [Postman Collection](link)
- [OpenAPI Spec](link)
- [Vendor Changelog](link)

## Notes

### Known Issues
- Issue 1: [description and workaround]
- Issue 2: [description and workaround]

### Tips
- Tip 1: [optimization or usage tip]
- Tip 2: [optimization or usage tip]
```

## Integration Categories

### Core Services
- `dify-api.md`
- `openai-api.md`
- `supabase.md`
- `postgres.md`

### Development Tools
- `github.md`
- `vercel.md`
- `docker.md`
- `kubernetes.md`

### Monitoring & Analytics
- `datadog.md`
- `sentry.md`
- `mixpanel.md`
- `google-analytics.md`

### Communication
- `slack.md`
- `sendgrid.md`
- `twilio.md`
- `discord.md`

### Payment & Commerce
- `stripe.md`
- `shopify.md`
- `paypal.md`

## Best Practices

1. **No Secrets**: Never commit actual credentials
2. **Environment Isolation**: Separate configs per environment
3. **Version Everything**: Track API versions explicitly
4. **Monitor Always**: Set up alerts before issues
5. **Document Changes**: Update when anything changes

## Review Checklist

- [ ] Credentials rotated per schedule?
- [ ] Usage within limits?
- [ ] Costs as expected?
- [ ] Performance acceptable?
- [ ] Backups configured?
- [ ] Monitoring active?
- [ ] Documentation current?
- [ ] Contacts updated?