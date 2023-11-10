# SpiderAM
SpiderAM offers a holistic approach to website monitoring, empowering users to make informed decisions regarding a website's operational status, hosting configuration, and potential security measures. It is a valuable tool for website administrators and developers seeking a comprehensive assessment of their online services.
SpiderAM was originally developed to assess the operational status of websites, with a focus on providing comprehensive insights into their functionality and hosting environment. It recognizes the challenges associated with solely relying on basic ping checks, which can yield false positives if the ping is obstructed. Additionally, determining the hosting service provider can be a complex task. However, this script offers a multi-faceted approach to address these challenges:

## 1.	CNAME & A Records:
The script extracts both A (Address) and CNAME (Canonical Name) records for a website, providing essential information about its DNS configuration.

## 2. Port Availability: 
It diligently examines open ports, offering a clear view of port status, including Port 80 and Port 443. This data is crucial for assessing a website's accessibility.

## 3. Server Vitality:
The script delves deeper by analyzing HTTP headers to ascertain the server's responsiveness. This goes beyond mere connectivity to determine if the server is genuinely active.

## 4. Website Exploration: 
It takes the analysis a step further by opening the website and retrieving its title. This enables users to gauge the probability of a live website based on its content.

## 5. Web Application Firewall Detection:
The script is equipped to identify the presence of a Web Application Firewall. it promises an added layer of insight into a website's security.

## Installation Guidelines:
Verify the presence of Python on your system.

It is essential to have a CSV file named hostnames.csv containing the list of website hostnames. Ensure the hostnames are listed in a single column without any headers.

#### 1st Step
```
pip install -r requirements.txt
```

Commence by opening your command prompt or terminal, Navigate to the directory where the script resides. Execute the script using the following command:

#### 2nd Step
```
cd /Users/YourUserName/Desktop/
```

#### 3rd Step 
```
python3 spiderAM.py 
```

or 

```
python spiderAM.py 
```

### Monitoring Progress:
The program initiates the monitoring process and keeps you informed with a progress percentage, indicating the extent of completion.

### Viewing Results:
Upon successful completion of the monitoring, the script generates an output in the form of a CSV file named results.csv. This file is a treasure trove of detailed information regarding the monitored websites.

### Sample Output CSV Format:
The generated results.csv file incorporates the following columns:

1.	Hostname
2.	CNAME (Canonical Name)
3.	Value IP
4.	Value Ping
5.	Status Port 80
6.	Status Port 443
7.	Status Page Title
8.	HTTP Headers
9.	WAF Detection
10. Service Probabilities
`
