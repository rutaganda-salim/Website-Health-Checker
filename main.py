import os
from dotenv import load_dotenv
from datetime import datetime
import requests
import whois

# Load environment variables
load_dotenv()

# Get URLs and interval from environment variables
urls = os.getenv('URLS').split(',')
interval_hours = int(os.getenv('CHECK_INTERVAL_HOURS'))

def check_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        speed = response.elapsed.total_seconds()
        return {
            'status': 'UP',
            'speed': f'{speed:.2f} seconds',
            'title': 'Unknown',
            'meta_description': 'No meta description',
            'domain_expiry': 'N/A'
        }
    except requests.RequestException:
        return {
            'status': 'DOWN',
            'speed': 'N/A',
            'title': 'N/A',
            'meta_description': 'N/A',
            'domain_expiry': 'N/A'
        }

def get_domain_expiry(url):
    domain = url.split('//')[1]
    try:
        domain_info = whois.whois(domain)
        expiry_date = domain_info.expiration_date
        if isinstance(expiry_date, list):
            expiry_date = expiry_date[0]
        return expiry_date.strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return 'None'

def generate_report():
    date_today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    report_lines = [
        'Website Health Report',
        '==================================================',
        f'Date: {date_today}\n'
    ]
    
    for url in urls:
        result = check_website(url)
        domain_expiry = get_domain_expiry(url)
        report_lines.append(f'Checking {url}...')
        report_lines.append(f'[{result["status"]}] {url} is reachable.')
        report_lines.append(f'[SPEED] {url} loaded in {result["speed"]}.')
        report_lines.append(f'[SEO] Title: {result["title"]}')
        report_lines.append(f'[SEO] Meta Description: {result["meta_description"]}')
        report_lines.append(f'[DOMAIN] Domain {url.split("//")[1]} expires on {domain_expiry}.')
        report_lines.append('--------------------------------------------------')

    return '\n'.join(report_lines)

if __name__ == '__main__':
    report = generate_report()
    with open('website_health_report.txt', 'w') as file:
        file.write(report)
