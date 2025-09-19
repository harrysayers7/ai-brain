#!/usr/bin/env python3
"""
Infrastructure Scanner
Automatically scans the infrastructure directory and updates INFRASTRUCTURE-OVERVIEW.md
with current state, services, and configurations.
"""

import os
import sys
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
from collections import defaultdict

try:
    import frontmatter
    import yaml
except ImportError:
    print("Please install required dependencies: pip install python-frontmatter pyyaml")
    sys.exit(1)


class InfrastructureScanner:
    """Scans infrastructure directory and generates comprehensive overview"""
    
    def __init__(self, root_path: str = "."):
        self.root = Path(root_path)
        self.infrastructure_dir = self.root / "infrastructure"
        self.overview_file = self.infrastructure_dir / "INFRASTRUCTURE-OVERVIEW.md"
        
        # Scan results
        self.scan_results = {
            'environments': {},
            'services': {},
            'networking': {},
            'security': {},
            'containers': {},
            'mcp_servers': {},
            'cloud_services': {},
            'databases': {},
            'monitoring': {},
            'statistics': {}
        }
    
    def scan_infrastructure(self):
        """Main scan function that orchestrates all scanning operations"""
        print("🔍 Starting infrastructure scan...")
        
        # Scan all infrastructure components
        self.scan_environments()
        self.scan_services()
        self.scan_networking()
        self.scan_security()
        self.scan_containers()
        self.scan_mcp_servers()
        self.scan_cloud_services()
        self.scan_databases()
        self.scan_monitoring()
        self.calculate_statistics()
        
        print("✅ Infrastructure scan complete")
    
    def scan_environments(self):
        """Scan environment configurations"""
        print("📁 Scanning environments...")
        
        env_dir = self.infrastructure_dir / "environments"
        if not env_dir.exists():
            return
        
        for env_folder in env_dir.iterdir():
            if env_folder.is_dir():
                env_name = env_folder.name
                env_info = {
                    'path': str(env_folder.relative_to(self.infrastructure_dir)),
                    'files': [],
                    'configs': {},
                    'status': 'unknown'
                }
                
                # Scan files in environment
                for file_path in env_folder.rglob("*.md"):
                    if file_path.is_file():
                        file_info = self.analyze_markdown_file(file_path)
                        env_info['files'].append(file_info)
                        
                        # Extract configuration data
                        if 'config' in file_info.get('tags', []):
                            env_info['configs'][file_path.stem] = file_info
                
                # Determine environment status
                if env_name == 'local':
                    env_info['status'] = 'active'
                elif env_name == 'production':
                    env_info['status'] = 'active'
                elif env_name == 'staging':
                    env_info['status'] = 'configured'
                
                self.scan_results['environments'][env_name] = env_info
    
    def scan_services(self):
        """Scan service configurations"""
        print("🔧 Scanning services...")
        
        services_dir = self.infrastructure_dir / "services"
        if not services_dir.exists():
            return
        
        for service_folder in services_dir.iterdir():
            if service_folder.is_dir():
                service_name = service_folder.name
                service_info = {
                    'path': str(service_folder.relative_to(self.infrastructure_dir)),
                    'files': [],
                    'configs': {},
                    'type': service_name
                }
                
                # Scan service files
                for file_path in service_folder.rglob("*.md"):
                    if file_path.is_file():
                        file_info = self.analyze_markdown_file(file_path)
                        service_info['files'].append(file_info)
                        
                        # Extract service-specific data
                        if 'database' in service_name:
                            service_info['configs'].update(self.extract_database_config(file_info))
                        elif 'cloud' in service_name:
                            service_info['configs'].update(self.extract_cloud_config(file_info))
                        elif 'monitoring' in service_name:
                            service_info['configs'].update(self.extract_monitoring_config(file_info))
                
                self.scan_results['services'][service_name] = service_info
    
    def scan_networking(self):
        """Scan networking configurations"""
        print("🌐 Scanning networking...")
        
        networking_dir = self.infrastructure_dir / "networking"
        if not networking_dir.exists():
            return
        
        networking_info = {
            'ports': [],
            'firewall_rules': [],
            'load_balancer': {},
            'vpn': {}
        }
        
        for file_path in networking_dir.rglob("*.md"):
            if file_path.is_file():
                file_info = self.analyze_markdown_file(file_path)
                
                # Extract port information
                if 'ports' in file_path.name.lower():
                    networking_info['ports'].extend(self.extract_ports(file_info))
                
                # Extract firewall rules
                if 'firewall' in file_info.get('content', '').lower():
                    networking_info['firewall_rules'].extend(self.extract_firewall_rules(file_info))
        
        self.scan_results['networking'] = networking_info
    
    def scan_security(self):
        """Scan security configurations"""
        print("🔒 Scanning security...")
        
        security_dir = self.infrastructure_dir / "security"
        if not security_dir.exists():
            return
        
        security_info = {
            'ssh_keys': [],
            'certificates': [],
            'access_control': {}
        }
        
        for file_path in security_dir.rglob("*.md"):
            if file_path.is_file():
                file_info = self.analyze_markdown_file(file_path)
                
                # Extract SSH key information
                if 'ssh' in file_path.name.lower():
                    security_info['ssh_keys'].extend(self.extract_ssh_keys(file_info))
                
                # Extract certificate information
                if 'cert' in file_path.name.lower():
                    security_info['certificates'].extend(self.extract_certificates(file_info))
        
        self.scan_results['security'] = security_info
    
    def scan_containers(self):
        """Scan container configurations"""
        print("🐳 Scanning containers...")
        
        containers_dir = self.infrastructure_dir / "containers"
        if not containers_dir.exists():
            return
        
        container_info = {
            'docker_compose_files': [],
            'dockerfiles': [],
            'kubernetes': []
        }
        
        for file_path in containers_dir.rglob("*"):
            if file_path.is_file():
                if file_path.name == 'docker-compose.yml':
                    container_info['docker_compose_files'].append({
                        'path': str(file_path.relative_to(self.infrastructure_dir)),
                        'services': self.extract_docker_services(file_path)
                    })
                elif file_path.name == 'Dockerfile':
                    container_info['dockerfiles'].append({
                        'path': str(file_path.relative_to(self.infrastructure_dir)),
                        'base_image': self.extract_dockerfile_base(file_path)
                    })
        
        self.scan_results['containers'] = container_info
    
    def scan_mcp_servers(self):
        """Scan MCP server configurations"""
        print("🤖 Scanning MCP servers...")
        
        mcp_dir = self.infrastructure_dir / "services" / "mcp"
        if not mcp_dir.exists():
            return
        
        mcp_info = {
            'production_servers': [],
            'local_servers': [],
            'configurations': []
        }
        
        # Scan MCP index file
        mcp_index = mcp_dir / "MCP-index.md"
        if mcp_index.exists():
            mcp_info['configurations'].append(self.analyze_markdown_file(mcp_index))
        
        # Scan individual MCP server configs
        mcp_servers_dir = mcp_dir / "mcp-servers"
        if mcp_servers_dir.exists():
            for server_file in mcp_servers_dir.rglob("*.md"):
                if server_file.is_file():
                    server_info = self.analyze_markdown_file(server_file)
                    server_info['name'] = server_file.stem
                    mcp_info['local_servers'].append(server_info)
        
        self.scan_results['mcp_servers'] = mcp_info
    
    def scan_cloud_services(self):
        """Scan cloud service configurations"""
        print("☁️ Scanning cloud services...")
        
        cloud_dir = self.infrastructure_dir / "services" / "cloud"
        if not cloud_dir.exists():
            return
        
        cloud_info = {
            'aws': {},
            'vercel': {},
            'cloudflare': {}
        }
        
        for cloud_file in cloud_dir.rglob("*.md"):
            if cloud_file.is_file():
                file_info = self.analyze_markdown_file(cloud_file)
                cloud_name = cloud_file.stem
                
                if cloud_name in cloud_info:
                    cloud_info[cloud_name] = file_info
        
        self.scan_results['cloud_services'] = cloud_info
    
    def scan_databases(self):
        """Scan database configurations"""
        print("🗄️ Scanning databases...")
        
        db_dir = self.infrastructure_dir / "services" / "databases"
        if not db_dir.exists():
            return
        
        db_info = {
            'postgresql': {},
            'redis': {},
            'supabase': {}
        }
        
        for db_file in db_dir.rglob("*.md"):
            if db_file.is_file():
                file_info = self.analyze_markdown_file(db_file)
                db_name = db_file.stem
                
                if db_name in db_info:
                    db_info[db_name] = file_info
        
        self.scan_results['databases'] = db_info
    
    def scan_monitoring(self):
        """Scan monitoring configurations"""
        print("📊 Scanning monitoring...")
        
        monitoring_dir = self.infrastructure_dir / "services" / "monitoring"
        if not monitoring_dir.exists():
            return
        
        monitoring_info = {
            'health_checks': [],
            'metrics': [],
            'alerting': []
        }
        
        for monitor_file in monitoring_dir.rglob("*.md"):
            if monitor_file.is_file():
                file_info = self.analyze_markdown_file(monitor_file)
                
                if 'mcp' in monitor_file.name.lower():
                    monitoring_info['health_checks'].extend(self.extract_health_checks(file_info))
                    monitoring_info['metrics'].extend(self.extract_metrics(file_info))
                    monitoring_info['alerting'].extend(self.extract_alerting(file_info))
        
        self.scan_results['monitoring'] = monitoring_info
    
    def calculate_statistics(self):
        """Calculate infrastructure statistics"""
        print("📈 Calculating statistics...")
        
        stats = {
            'total_environments': len(self.scan_results['environments']),
            'total_services': len(self.scan_results['services']),
            'total_mcp_servers': len(self.scan_results['mcp_servers'].get('local_servers', [])),
            'total_databases': len(self.scan_results['databases']),
            'total_cloud_services': len(self.scan_results['cloud_services']),
            'total_config_files': 0,
            'last_scan': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Count configuration files
        for env in self.scan_results['environments'].values():
            stats['total_config_files'] += len(env.get('files', []))
        
        for service in self.scan_results['services'].values():
            stats['total_config_files'] += len(service.get('files', []))
        
        self.scan_results['statistics'] = stats
    
    def analyze_markdown_file(self, file_path: Path) -> Dict[str, Any]:
        """Analyze a markdown file and extract metadata"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse frontmatter
            post = frontmatter.loads(content)
            metadata = post.metadata
            
            return {
                'path': str(file_path.relative_to(self.infrastructure_dir)),
                'title': metadata.get('title', file_path.stem),
                'type': metadata.get('type', 'unknown'),
                'subtype': metadata.get('subtype', 'unknown'),
                'tags': metadata.get('tags', []),
                'created': metadata.get('created', ''),
                'modified': metadata.get('modified', ''),
                'version': metadata.get('version', 1),
                'ship_factor': metadata.get('ship_factor', 5),
                'content': post.content,
                'size': len(content)
            }
        except Exception as e:
            print(f"Warning: Could not analyze {file_path}: {e}")
            return {
                'path': str(file_path.relative_to(self.infrastructure_dir)),
                'title': file_path.stem,
                'type': 'unknown',
                'subtype': 'unknown',
                'tags': [],
                'created': '',
                'modified': '',
                'version': 1,
                'ship_factor': 5,
                'content': '',
                'size': 0
            }
    
    def extract_ports(self, file_info: Dict) -> List[Dict]:
        """Extract port information from file content"""
        ports = []
        content = file_info.get('content', '')
        
        # Look for port patterns in YAML blocks
        yaml_blocks = re.findall(r'```yaml\n(.*?)\n```', content, re.DOTALL)
        for block in yaml_blocks:
            # Simple port extraction - can be enhanced
            port_matches = re.findall(r'port:\s*(\d+)', block)
            for port in port_matches:
                ports.append({'port': int(port), 'service': 'unknown'})
        
        return ports
    
    def extract_firewall_rules(self, file_info: Dict) -> List[Dict]:
        """Extract firewall rules from file content"""
        rules = []
        content = file_info.get('content', '')
        
        # Look for firewall rule patterns
        rule_matches = re.findall(r'-\s*port:\s*(\d+).*?action:\s*(\w+)', content)
        for port, action in rule_matches:
            rules.append({'port': int(port), 'action': action})
        
        return rules
    
    def extract_ssh_keys(self, file_info: Dict) -> List[Dict]:
        """Extract SSH key information from file content"""
        keys = []
        content = file_info.get('content', '')
        
        # Look for SSH key patterns
        key_matches = re.findall(r'name:\s*([^\n]+).*?location:\s*([^\n]+)', content, re.DOTALL)
        for name, location in key_matches:
            keys.append({'name': name.strip(), 'location': location.strip()})
        
        return keys
    
    def extract_certificates(self, file_info: Dict) -> List[Dict]:
        """Extract certificate information from file content"""
        certs = []
        content = file_info.get('content', '')
        
        # Look for certificate patterns
        cert_matches = re.findall(r'domain:\s*([^\n]+).*?expires:\s*([^\n]+)', content, re.DOTALL)
        for domain, expires in cert_matches:
            certs.append({'domain': domain.strip(), 'expires': expires.strip()})
        
        return certs
    
    def extract_docker_services(self, file_path: Path) -> List[Dict]:
        """Extract Docker services from docker-compose.yml"""
        services = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple service extraction - can be enhanced with proper YAML parsing
            service_matches = re.findall(r'(\w+):\s*\n\s*image:\s*([^\n]+)', content)
            for name, image in service_matches:
                services.append({'name': name, 'image': image.strip()})
        except Exception as e:
            print(f"Warning: Could not parse {file_path}: {e}")
        
        return services
    
    def extract_dockerfile_base(self, file_path: Path) -> str:
        """Extract base image from Dockerfile"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().startswith('FROM '):
                        return line.strip().split(' ', 1)[1]
        except Exception as e:
            print(f"Warning: Could not parse {file_path}: {e}")
        
        return 'unknown'
    
    def extract_database_config(self, file_info: Dict) -> Dict:
        """Extract database configuration from file info"""
        config = {}
        content = file_info.get('content', '')
        
        # Extract database connection info
        if 'postgresql' in content.lower():
            config['type'] = 'postgresql'
        elif 'redis' in content.lower():
            config['type'] = 'redis'
        elif 'supabase' in content.lower():
            config['type'] = 'supabase'
        
        return config
    
    def extract_cloud_config(self, file_info: Dict) -> Dict:
        """Extract cloud configuration from file info"""
        config = {}
        content = file_info.get('content', '')
        
        # Extract cloud service info
        if 'aws' in content.lower():
            config['provider'] = 'aws'
        elif 'vercel' in content.lower():
            config['provider'] = 'vercel'
        elif 'cloudflare' in content.lower():
            config['provider'] = 'cloudflare'
        
        return config
    
    def extract_monitoring_config(self, file_info: Dict) -> Dict:
        """Extract monitoring configuration from file info"""
        config = {}
        content = file_info.get('content', '')
        
        # Extract monitoring tools
        if 'prometheus' in content.lower():
            config['metrics'] = 'prometheus'
        if 'grafana' in content.lower():
            config['visualization'] = 'grafana'
        if 'health' in content.lower():
            config['health_checks'] = True
        
        return config
    
    def extract_health_checks(self, file_info: Dict) -> List[Dict]:
        """Extract health check configurations"""
        checks = []
        content = file_info.get('content', '')
        
        # Look for health check patterns
        check_matches = re.findall(r'url:\s*([^\n]+).*?interval:\s*([^\n]+)', content, re.DOTALL)
        for url, interval in check_matches:
            checks.append({'url': url.strip(), 'interval': interval.strip()})
        
        return checks
    
    def extract_metrics(self, file_info: Dict) -> List[Dict]:
        """Extract metrics configurations"""
        metrics = []
        content = file_info.get('content', '')
        
        # Look for metrics patterns
        metric_matches = re.findall(r'name:\s*([^\n]+).*?type:\s*([^\n]+)', content, re.DOTALL)
        for name, metric_type in metric_matches:
            metrics.append({'name': name.strip(), 'type': metric_type.strip()})
        
        return metrics
    
    def extract_alerting(self, file_info: Dict) -> List[Dict]:
        """Extract alerting configurations"""
        alerts = []
        content = file_info.get('content', '')
        
        # Look for alert patterns
        alert_matches = re.findall(r'name:\s*([^\n]+).*?severity:\s*([^\n]+)', content, re.DOTALL)
        for name, severity in alert_matches:
            alerts.append({'name': name.strip(), 'severity': severity.strip()})
        
        return alerts
    
    def generate_updated_overview(self) -> str:
        """Generate updated INFRASTRUCTURE-OVERVIEW.md content"""
        print("📝 Generating updated infrastructure overview...")
        
        # Load template
        with open(self.overview_file, 'r', encoding='utf-8') as f:
            template = f.read()
        
        # Replace auto-updated placeholders
        replacements = {
            '[AUTO-UPDATED]': self.scan_results['statistics']['last_scan'],
            '**Total Components**: [AUTO-UPDATED]': f"**Total Components**: {self.scan_results['statistics']['total_config_files']}",
            '**Total Environments**: [AUTO-UPDATED]': f"**Total Environments**: {self.scan_results['statistics']['total_environments']}",
            '**Active Services**: [AUTO-UPDATED]': f"**Active Services**: {self.scan_results['statistics']['total_services']}",
            '**MCP Servers**: [AUTO-UPDATED]': f"**MCP Servers**: {self.scan_results['statistics']['total_mcp_servers']}",
            '**Database Instances**: [AUTO-UPDATED]': f"**Database Instances**: {self.scan_results['statistics']['total_databases']}",
            '**Cloud Services**: [AUTO-UPDATED]': f"**Cloud Services**: {self.scan_results['statistics']['total_cloud_services']}",
            '**Configuration Files**: [AUTO-UPDATED]': f"**Configuration Files**: {self.scan_results['statistics']['total_config_files']}",
            '**Last Scan**: [AUTO-UPDATED]': f"**Last Scan**: {self.scan_results['statistics']['last_scan']}"
        }
        
        # Apply replacements
        updated_content = template
        for placeholder, replacement in replacements.items():
            updated_content = updated_content.replace(placeholder, replacement)
        
        # Update environment sections
        updated_content = self.update_environment_sections(updated_content)
        updated_content = self.update_service_sections(updated_content)
        updated_content = self.update_network_sections(updated_content)
        updated_content = self.update_mcp_sections(updated_content)
        updated_content = self.update_cloud_sections(updated_content)
        updated_content = self.update_database_sections(updated_content)
        
        return updated_content
    
    def update_environment_sections(self, content: str) -> str:
        """Update environment-specific sections"""
        # Update local development section
        local_env = self.scan_results['environments'].get('local', {})
        if local_env:
            # Extract active services from local environment
            active_services = []
            for file_info in local_env.get('files', []):
                if 'redis' in file_info.get('content', '').lower():
                    active_services.append('Redis Server - Port 6379 (Active)')
                if 'postgresql' in file_info.get('content', '').lower():
                    active_services.append('PostgreSQL 15 - Installed, ready to start')
                if 'docker' in file_info.get('content', '').lower():
                    active_services.append('Docker Desktop - Available')
            
            # Update the content
            if active_services:
                services_text = '\n'.join([f"- **{service}**" for service in active_services])
                content = re.sub(
                    r'### Local Development\n.*?\n\n',
                    f'### Local Development\n{services_text}\n\n',
                    content,
                    flags=re.DOTALL
                )
        
        return content
    
    def update_service_sections(self, content: str) -> str:
        """Update service-specific sections"""
        # This can be enhanced to update specific service information
        return content
    
    def update_network_sections(self, content: str) -> str:
        """Update network configuration sections"""
        # This can be enhanced to update port and network information
        return content
    
    def update_mcp_sections(self, content: str) -> str:
        """Update MCP server sections"""
        mcp_servers = self.scan_results['mcp_servers']
        local_servers = mcp_servers.get('local_servers', [])
        
        if local_servers:
            # Generate MCP server list
            server_list = []
            for server in local_servers:
                name = server.get('name', 'unknown')
                title = server.get('title', name)
                server_list.append(f"- **{title}** - {name}")
            
            # Update the content
            servers_text = '\n'.join(server_list)
            content = re.sub(
                r'### Local Development Servers\n.*?\n\n',
                f'### Local Development Servers\n{servers_text}\n\n',
                content,
                flags=re.DOTALL
            )
        
        return content
    
    def update_cloud_sections(self, content: str) -> str:
        """Update cloud service sections"""
        # This can be enhanced to update cloud service information
        return content
    
    def update_database_sections(self, content: str) -> str:
        """Update database sections"""
        # This can be enhanced to update database information
        return content
    
    def update_overview_file(self):
        """Update the INFRASTRUCTURE-OVERVIEW.md file"""
        print("🔄 Updating infrastructure overview file...")
        
        # Generate updated content
        updated_content = self.generate_updated_overview()
        
        # Write to file
        with open(self.overview_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print("✅ Infrastructure overview updated successfully")
    
    def generate_scan_report(self) -> str:
        """Generate a detailed scan report"""
        report = [
            "# Infrastructure Scan Report",
            f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*",
            "",
            "## Scan Summary",
            f"- **Total Environments**: {self.scan_results['statistics']['total_environments']}",
            f"- **Total Services**: {self.scan_results['statistics']['total_services']}",
            f"- **Total MCP Servers**: {self.scan_results['statistics']['total_mcp_servers']}",
            f"- **Total Databases**: {self.scan_results['statistics']['total_databases']}",
            f"- **Total Cloud Services**: {self.scan_results['statistics']['total_cloud_services']}",
            f"- **Total Config Files**: {self.scan_results['statistics']['total_config_files']}",
            "",
            "## Environment Details",
            ""
        ]
        
        for env_name, env_info in self.scan_results['environments'].items():
            report.append(f"### {env_name.title()}")
            report.append(f"- **Path**: `{env_info['path']}`")
            report.append(f"- **Status**: {env_info['status']}")
            report.append(f"- **Files**: {len(env_info['files'])}")
            report.append("")
        
        report.extend([
            "## Service Details",
            ""
        ])
        
        for service_name, service_info in self.scan_results['services'].items():
            report.append(f"### {service_name.title()}")
            report.append(f"- **Path**: `{service_info['path']}`")
            report.append(f"- **Type**: {service_info['type']}")
            report.append(f"- **Files**: {len(service_info['files'])}")
            report.append("")
        
        return '\n'.join(report)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Infrastructure Scanner")
    parser.add_argument('--scan', action='store_true', help='Scan infrastructure and update overview')
    parser.add_argument('--report', action='store_true', help='Generate detailed scan report')
    parser.add_argument('--report-file', default='infrastructure-scan-report.md', help='Output file for scan report')
    parser.add_argument('--root', default='.', help='Root directory path')
    
    args = parser.parse_args()
    
    scanner = InfrastructureScanner(args.root)
    
    if args.scan:
        scanner.scan_infrastructure()
        scanner.update_overview_file()
    
    if args.report:
        scanner.scan_infrastructure()
        report = scanner.generate_scan_report()
        report_file = Path(args.root) / args.report_file
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"📊 Scan report saved to {report_file}")
    
    if not args.scan and not args.report:
        print("Use --scan to update infrastructure overview or --report to generate scan report")


if __name__ == "__main__":
    main()
