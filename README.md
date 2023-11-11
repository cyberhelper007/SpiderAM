# SpiderAM
SpiderAM offers a holistic approach to website monitoring, empowering users to make informed decisions regarding a website's operational status, hosting configuration, and potential security measures. It is a valuable tool for website administrators and developers seeking a comprehensive assessment of their online services.
SpiderAM was originally developed to assess the operational status of websites, with a focus on providing comprehensive insights into their functionality and hosting environment. It recognizes the challenges associated with solely relying on basic ping checks, which can yield false positives if the ping is obstructed. Additionally, determining the hosting service provider can be a complex task. However, this script offers a multi-faceted approach to address these challenges:

## Viewing Output / Results:
Upon the successful conclusion of the monitoring process, the script produces a `CSV file` named <strong>results.csv</strong>. Within this file lies a wealth of intricate details pertaining to the monitored websites. Ultimately, this culminates in the creation of an `output file` results.csv, providing a convenient avenue for effortless examination and analysis of the acquired results using Excel.
![Viewing Output Results](https://github.com/cyberhelper007/SpiderAM/assets/150381883/2191022e-54e0-4d72-a393-ab9dae79081f)
#### Sample Output CSV Format:
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

## How does it Work?
#### 1.	CNAME & A Records:
The script extracts both A (Address) and CNAME (Canonical Name) records for a website, providing essential information about its DNS configuration.
#### 2. Port Availability: 
It diligently examines open ports, offering a clear view of port status, including Port 80 and Port 443. This data is crucial for assessing a website's accessibility.
#### 3. Server Vitality:
The script delves deeper by analyzing HTTP headers to ascertain the server's responsiveness. This goes beyond mere connectivity to determine if the server is genuinely active.
#### 4. Website Exploration: 
It takes the analysis a step further by opening the website and retrieving its title. This enables users to gauge the probability of a live website based on its content.
#### 5. Web Application Firewall Detection:
The script is equipped to identify the presence of a Web Application Firewall. it promises an added layer of insight into a website's security.


## Installation Guidelines:
Verify the presence of Python on your system.

### 1st Step

Commence by opening your command prompt or terminal, "Navigate to the directory" where the script resides. 
```
cd /Users/Your_Patch/SpiderAM-main
```

Ensure that you install the dependencies for this application by executing the command specified below.

```
pip install -r requirements.txt
```

### 2nd Step
It is essential to have a CSV file named hostnames.csv containing the list of website hostnames.
##### open the file "hostnames.csv" in the text editor or spreadsheet editor such as microsoft excel
Ensure the hostnames are listed in a single column without any headers.


### 3rd Step 
Execute the script using the following command:

```
python3 spiderAM.py 
```

or 

```
python spiderAM.py 
```

## Monitoring Progress:
The program initiates the monitoring process and keeps you informed with a progress percentage, indicating the extent of completion:

![image](https://github.com/cyberhelper007/SpiderAM/assets/150381883/43af1890-0d4f-4936-8be5-de422d2905e8)
