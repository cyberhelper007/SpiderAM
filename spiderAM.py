#Wellcome to Spideram The Spideram offers a holistic approach to website monitoring, empowering users 
#to make informed decisions regarding a website's operational status, hosting configuration, and potential security measures. 

import csv
import subprocess
import socket
import dns.resolver
import requests
from bs4 import BeautifulSoup
from wafw00f.main import WAFW00F

def check_waf(target):
    cmd = ['WafW00F', target]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out, err = process.communicate()

    lines = out.decode().split('\n')

    for line in lines:
        if line.startswith('[+]'):
            waf = line.split('behind ')[-1]
            break
    else:
        waf = 'No WAF detected'

    return waf

def checkWAF(host):
    try:
        waf = check_waf(host)
        return waf
    except Exception as e:
        return f"WAF detection error: {str(e)}"

def checkPING(host):
    try:
        ping = subprocess.check_output(['ping', '-c2', host])
        return "Host is UP"
    except:
        return "Host is DOWN"

def checkPort(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, port))
        return f"Port {port} is open"
    except:
        return f"Port {port} is closed"

def getHTTPHeaders(host):
    try:
        response = requests.get('https://' + host, timeout=1)
        headers = response.headers
    except:
        try:
            response = requests.get('http://' + host, timeout=1)
            headers = response.headers
        except:
            return "Unable to retrieve headers"

    useful_info = {
        'Server': headers.get('Server', 'N/A'),
        'X-Powered-By': headers.get('X-Powered-By', 'N/A'),
    }
    return useful_info

def getPageTitle(host):
    try:
        response = requests.get('http://' + host, timeout=1)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip()
        return title
    except:
        try:
            # If the title cannot be retrieved, try to get the first H1, H2, H3, or H4 header
            soup = BeautifulSoup(response.text, 'html.parser')
            header_tags = soup.find_all(['h1', 'h2', 'h3', 'h4'])
            if header_tags:
                return header_tags[0].text.strip()
            else:
                return "No headers found"
        except:
            return "No headers found"

def checkDNS(host):
    try:
        ip = socket.gethostbyname(host)
        return ip
    except:
        return "No DNS entry found"

def getCNAMERecord(host):
    try:
        result = dns.resolver.resolve(host, 'CNAME')
        cname_value = result[0].target.to_text() if result else "N/A"
        return cname_value
    except:
        return "N/A"

def calculate_service_probabilities(ping_status, port_80_status, port_443_status, headers, title):
    probabilities = 0

    if "Host is UP" in ping_status:
        probabilities += 12.5

    if "Port 80 is open" in port_80_status:
        probabilities += 12.5

    if "Port 443 is open" in port_443_status:
        probabilities += 25

    if "Unable to retrieve headers" not in title:
        probabilities += 25

    if "Server" in headers:
        probabilities += 25

    return "{:.2f}%".format(probabilities)

csv_file_path = 'hostnames.csv'
host_list = []

with open(csv_file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for i in row:
            host_list.append(i.strip())

total_hosts = len(host_list)

output_data = []

for index, host in enumerate(host_list):
    progress = (index + 1) / total_hosts * 100
    print(f"Progress: {progress:.2f}%")

    ping_status = checkPING(host)
    port_80_status = checkPort(host, 80)
    port_443_status = checkPort(host, 443)
    headers = getHTTPHeaders(host)
    title = getPageTitle(host)
    ip_value = checkDNS(host)
    cname_value = getCNAMERecord(host)
    waf_status = checkWAF(host)

    probabilities = calculate_service_probabilities(ping_status, port_80_status, port_443_status, headers, title)

    output_data.append([host, cname_value, ip_value, ping_status, port_80_status, port_443_status, title, headers, waf_status, probabilities])

output_csv_file_path = 'results.csv'

# Write data to CSV file
with open(output_csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Hostname', 'CNAME', 'Value IP', 'Value Ping', 'Status Port 80', 'Status Port 443', 'Status Page Title', 'HTTP Headers', 'WAF Detection', 'Service Probabilities'])
    writer.writerows(output_data)

print("Script completed.")
