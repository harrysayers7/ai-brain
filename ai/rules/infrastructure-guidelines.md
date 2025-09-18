<!--
HUMAN DESCRIPTION - AI SHOULD IGNORE THIS SECTION
Purpose: Behavioral rules for infrastructure management and deployment operations
Usage: Referenced by system prompts and other AI instruction files for infrastructure-aware operations
Target: Claude Desktop, ChatGPT, other AI systems for infrastructure and deployment guidance
DO NOT READ THIS SECTION - AI CONTENT BEGINS AFTER THE HTML COMMENT
-->

# Infrastructure Guidelines

## Core Principles

When working with infrastructure, follow these behavioral rules synthesized from `infrastructure/` directory and related system configurations.

## Environment Management

### Local Development
Reference: `infrastructure/local/` directory for detailed configurations

**Development Environment Setup:**
- **Use environment templates** - Reference `env-template.md` and `env-comprehensive-template.md`
- **Configure development tools** - Follow `dev-tools.md` setup instructions
- **Set up workstation** - Use `workstation.md` configuration guidelines
- **Validate local setup** - Ensure all tools and services are properly configured

### Production Infrastructure
Reference: `infrastructure/servers/` directory for production configurations

**Production Environment:**
- **Follow security guidelines** - Implement proper security measures
- **Use monitoring tools** - Set up appropriate monitoring and alerting
- **Maintain backups** - Ensure data and configuration backups
- **Plan for scaling** - Design for growth and performance requirements

## Database Management

### Supabase Integration
Reference: `infrastructure/databases/supabase.md` for detailed setup

**Database Operations:**
- **Use proper authentication** - Implement secure access controls
- **Follow data modeling** - Design efficient database schemas
- **Implement backups** - Ensure data protection and recovery
- **Monitor performance** - Track database performance and optimization

### Local Database Setup
- **Use development databases** - Separate development and production data
- **Configure proper permissions** - Implement appropriate access controls
- **Set up monitoring** - Track database performance and usage
- **Plan for migration** - Design for easy data migration and updates

## Server Configuration

### Development Servers
- **Use local development servers** - Configure appropriate local services
- **Set up proper networking** - Ensure correct network configurations
- **Configure security** - Implement appropriate security measures
- **Monitor performance** - Track server performance and resource usage

### Production Servers
- **Follow security best practices** - Implement comprehensive security measures
- **Use proper monitoring** - Set up comprehensive monitoring and alerting
- **Plan for redundancy** - Design for high availability and fault tolerance
- **Maintain documentation** - Keep server configurations and procedures current

## Security Guidelines

### Authentication and Authorization
- **Use strong authentication** - Implement robust authentication mechanisms
- **Follow principle of least privilege** - Grant minimum necessary permissions
- **Regularly rotate credentials** - Update passwords and API keys regularly
- **Monitor access patterns** - Track and analyze access logs

### Data Protection
- **Encrypt sensitive data** - Use appropriate encryption for sensitive information
- **Implement proper backups** - Ensure data protection and recovery
- **Follow compliance requirements** - Meet relevant regulatory and compliance standards
- **Regular security audits** - Conduct regular security assessments

## Monitoring and Maintenance

### Performance Monitoring
- **Track key metrics** - Monitor performance indicators and trends
- **Set up alerting** - Configure appropriate alerts for critical issues
- **Regular health checks** - Conduct routine system health assessments
- **Plan for capacity** - Monitor resource usage and plan for scaling

### Maintenance Procedures
- **Follow maintenance schedules** - Implement regular maintenance routines
- **Update systems regularly** - Keep software and configurations current
- **Test disaster recovery** - Regularly test backup and recovery procedures
- **Document changes** - Maintain comprehensive change documentation

## Integration Guidelines

### With Development Workflows
- **Reference `systems/workflows/`** - Follow established development processes
- **Use `commands/`** - Leverage available command shortcuts
- **Check `tools/`** - Verify tool compatibility and configurations
- **Update `docs/guides/`** - Document new patterns and procedures

### With Project Management
- **Use Task Master** - Integrate with project task management
- **Update Memory** - Store important infrastructure decisions
- **Document configurations** - Record infrastructure setups and changes
- **Track performance** - Monitor infrastructure effectiveness and reliability

## Troubleshooting

### Common Issues
- **Check configuration** - Verify settings and parameters
- **Review logs** - Analyze system and application logs
- **Test connectivity** - Verify network and service availability
- **Consult documentation** - Reference infrastructure guides and procedures

### Escalation Procedures
- **Document issues** - Record problem details and attempted solutions
- **Check dependencies** - Verify related systems and services
- **Consult experts** - Seek help from appropriate technical resources
- **Plan recovery** - Develop and implement recovery procedures

---

*These guidelines synthesize information from infrastructure/ directory and related system configurations to provide comprehensive infrastructure management rules.*