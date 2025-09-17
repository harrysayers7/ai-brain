#!/usr/bin/env python3
"""
Context File Notifier
Sends notifications when context files are updated.
Supports multiple notification methods: console, file, email, webhook.
"""

import os
import sys
import json
import smtplib
import requests
from datetime import datetime
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict, List, Optional


class ContextNotifier:
    """Send notifications about context file changes"""
    
    def __init__(self, root_path: str = "."):
        self.root = Path(root_path)
        self.config_file = self.root / '.context-notifier-config.json'
        self.load_config()
    
    def load_config(self):
        """Load notification configuration"""
        default_config = {
            'notifications': {
                'console': True,
                'file': True,
                'email': False,
                'webhook': False
            },
            'email': {
                'smtp_server': 'smtp.gmail.com',
                'smtp_port': 587,
                'username': '',
                'password': '',
                'from_email': '',
                'to_emails': []
            },
            'webhook': {
                'url': '',
                'headers': {},
                'timeout': 30
            },
            'file': {
                'log_file': 'context-updates.log',
                'max_size_mb': 10
            }
        }
        
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = {**default_config, **json.load(f)}
        else:
            self.config = default_config
            self.save_config()
    
    def save_config(self):
        """Save notification configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def format_notification(self, changes: Dict[str, Dict]) -> str:
        """Format notification message"""
        if not changes:
            return ""
        
        lines = []
        lines.append("🔔 Context Files Updated")
        lines.append(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        for name, change in changes.items():
            file_path = Path(change['file_path'])
            current_meta = change['current_metadata']
            
            lines.append(f"📝 **{name.replace('-', ' ').title()}**")
            lines.append(f"   File: `{file_path.relative_to(self.root)}`")
            lines.append(f"   Title: {current_meta.get('title', 'N/A')}")
            lines.append(f"   Version: {current_meta.get('version', 1)}")
            lines.append(f"   Ship Factor: {current_meta.get('ship_factor', 5)}")
            lines.append(f"   Size: {current_meta.get('size', 0)} bytes")
            lines.append("")
        
        return '\n'.join(lines)
    
    def notify_console(self, message: str):
        """Send notification to console"""
        if not self.config['notifications']['console']:
            return
        
        print("\n" + "="*50)
        print(message)
        print("="*50 + "\n")
    
    def notify_file(self, message: str):
        """Log notification to file"""
        if not self.config['notifications']['file']:
            return
        
        log_file = self.root / self.config['file']['log_file']
        max_size = self.config['file']['max_size_mb'] * 1024 * 1024
        
        # Check file size and rotate if needed
        if log_file.exists() and log_file.stat().st_size > max_size:
            backup_file = log_file.with_suffix('.log.backup')
            if backup_file.exists():
                backup_file.unlink()
            log_file.rename(backup_file)
        
        # Append to log file
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"\n{datetime.now().isoformat()}\n")
            f.write(message)
            f.write("\n" + "-"*50 + "\n")
    
    def notify_email(self, message: str):
        """Send notification via email"""
        if not self.config['notifications']['email']:
            return
        
        email_config = self.config['email']
        
        # Check if email is configured
        if not all([email_config['username'], email_config['password'], 
                   email_config['from_email'], email_config['to_emails']]):
            print("⚠️  Email notification not configured")
            return
        
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = email_config['from_email']
            msg['To'] = ', '.join(email_config['to_emails'])
            msg['Subject'] = f"Context Files Updated - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            
            # Add body
            msg.attach(MIMEText(message, 'plain'))
            
            # Send email
            server = smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port'])
            server.starttls()
            server.login(email_config['username'], email_config['password'])
            server.send_message(msg)
            server.quit()
            
            print("✅ Email notification sent")
            
        except Exception as e:
            print(f"❌ Failed to send email notification: {e}")
    
    def notify_webhook(self, message: str):
        """Send notification via webhook"""
        if not self.config['notifications']['webhook']:
            return
        
        webhook_config = self.config['webhook']
        
        if not webhook_config['url']:
            print("⚠️  Webhook URL not configured")
            return
        
        try:
            payload = {
                'text': message,
                'timestamp': datetime.now().isoformat(),
                'source': 'context-monitor'
            }
            
            response = requests.post(
                webhook_config['url'],
                json=payload,
                headers=webhook_config['headers'],
                timeout=webhook_config['timeout']
            )
            
            if response.status_code == 200:
                print("✅ Webhook notification sent")
            else:
                print(f"❌ Webhook notification failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Failed to send webhook notification: {e}")
    
    def send_notifications(self, changes: Dict[str, Dict]):
        """Send all configured notifications"""
        if not changes:
            return
        
        message = self.format_notification(changes)
        
        # Send all configured notifications
        self.notify_console(message)
        self.notify_file(message)
        self.notify_email(message)
        self.notify_webhook(message)
    
    def setup_email(self, smtp_server: str, smtp_port: int, username: str, 
                   password: str, from_email: str, to_emails: List[str]):
        """Setup email notification"""
        self.config['notifications']['email'] = True
        self.config['email'].update({
            'smtp_server': smtp_server,
            'smtp_port': smtp_port,
            'username': username,
            'password': password,
            'from_email': from_email,
            'to_emails': to_emails
        })
        self.save_config()
        print("✅ Email notification configured")
    
    def setup_webhook(self, url: str, headers: Dict = None):
        """Setup webhook notification"""
        self.config['notifications']['webhook'] = True
        self.config['webhook'].update({
            'url': url,
            'headers': headers or {}
        })
        self.save_config()
        print("✅ Webhook notification configured")
    
    def enable_notification(self, notification_type: str):
        """Enable a specific notification type"""
        if notification_type in self.config['notifications']:
            self.config['notifications'][notification_type] = True
            self.save_config()
            print(f"✅ {notification_type} notification enabled")
        else:
            print(f"❌ Unknown notification type: {notification_type}")
    
    def disable_notification(self, notification_type: str):
        """Disable a specific notification type"""
        if notification_type in self.config['notifications']:
            self.config['notifications'][notification_type] = False
            self.save_config()
            print(f"✅ {notification_type} notification disabled")
        else:
            print(f"❌ Unknown notification type: {notification_type}")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Context File Notifier")
    parser.add_argument('--setup-email', action='store_true', help='Setup email notifications')
    parser.add_argument('--setup-webhook', action='store_true', help='Setup webhook notifications')
    parser.add_argument('--enable', help='Enable notification type (console, file, email, webhook)')
    parser.add_argument('--disable', help='Disable notification type (console, file, email, webhook)')
    parser.add_argument('--test', action='store_true', help='Send test notification')
    parser.add_argument('--root', default='.', help='Root directory path')
    
    args = parser.parse_args()
    
    notifier = ContextNotifier(args.root)
    
    if args.setup_email:
        print("Setting up email notifications...")
        smtp_server = input("SMTP Server (e.g., smtp.gmail.com): ")
        smtp_port = int(input("SMTP Port (e.g., 587): "))
        username = input("Username: ")
        password = input("Password: ")
        from_email = input("From Email: ")
        to_emails = input("To Emails (comma-separated): ").split(',')
        to_emails = [email.strip() for email in to_emails]
        
        notifier.setup_email(smtp_server, smtp_port, username, password, from_email, to_emails)
    
    elif args.setup_webhook:
        print("Setting up webhook notifications...")
        url = input("Webhook URL: ")
        headers_input = input("Headers (JSON format, optional): ")
        headers = json.loads(headers_input) if headers_input else {}
        
        notifier.setup_webhook(url, headers)
    
    elif args.enable:
        notifier.enable_notification(args.enable)
    
    elif args.disable:
        notifier.disable_notification(args.disable)
    
    elif args.test:
        test_changes = {
            'infrastructure': {
                'file_path': 'ai/context/infrastructure.md',
                'current_metadata': {
                    'title': 'Infrastructure Context',
                    'version': 2,
                    'ship_factor': 8,
                    'size': 1024
                }
            }
        }
        notifier.send_notifications(test_changes)
    
    else:
        print("Context File Notifier")
        print("Use --help for available options")


if __name__ == "__main__":
    main()
