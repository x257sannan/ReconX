<div align="center">

# ReconX

### Automated Reconnaissance Framework

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

**A Python-based automated reconnaissance framework for penetration testing and security assessments.**

</div>

---

## About

ReconX is an automated reconnaissance framework developed in Python to simplify the information gathering phase of penetration testing. It integrates multiple security tools into a single framework to automate host discovery, service enumeration, web reconnaissance, vulnerability identification, and report generation.

The framework helps security professionals and students perform reconnaissance efficiently while reducing manual effort.

---
## Features

ReconX provides the following capabilities:

- Automated Nmap Port Scanning
- Service and Version Detection
- Operating System Detection
- DNS Enumeration
- WHOIS Lookup
- Web Server Detection
- Gobuster Directory Enumeration
- WhatWeb Technology Detection
- Nikto Web Vulnerability Scanning
- CVE Lookup
- Vulnerability Analysis
- Risk Analysis
- JSON Report Generation
- HTML Report Generation
- PDF Report Generation
- Logging System
- Modular Python Architecture

---

## Technologies Used

### Programming Language

- Python 3

### Operating System

- Kali Linux

### External Security Tools

- Nmap
- Nikto
- Gobuster
- WhatWeb

### Python Libraries

- argparse
- subprocess
- logging
- json
- csv
- os
- xml.etree.ElementTree

---

## Installation

Follow these steps to set up ReconX on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/x257sannan/ReconX.git
```

### 2. Navigate to the Project Directory

```bash
cd ReconX
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Required Security Tools

Make sure the following tools are installed on your Kali Linux system:

- Nmap
- Nikto
- Gobuster
- WhatWeb

Verify the installation:

```bash
nmap --version
nikto -Version
gobuster version
whatweb --version
```

---

## Usage

Run ReconX by providing the target hostname or IP address.

### Basic Scan

```bash
python3 reconx.py <target>
```

### Example

```bash
python3 reconx.py scanme.nmap.org
```

```bash
python3 reconx.py 192.168.1.100
```

### Output

After a successful scan, ReconX performs the following tasks:

- Performs an Nmap scan
- Detects open ports and running services
- Identifies the operating system
- Performs DNS and WHOIS lookup
- Detects web services
- Runs WhatWeb analysis
- Runs Gobuster directory enumeration
- Runs Nikto vulnerability scanning
- Performs CVE lookup
- Analyzes vulnerabilities and risk levels
- Generates JSON, HTML, and PDF reports
- Stores execution logs

---

## Workflow

ReconX follows the workflow below to automate the reconnaissance process:

```text
Start
   │
   ▼
User Enters Target
   │
   ▼
Run Nmap Scan
   │
   ▼
Parse XML Results
   │
   ▼
Identify Open Ports & Services
   │
   ▼
Operating System Detection
   │
   ▼
DNS Enumeration
   │
   ▼
WHOIS Lookup
   │
   ▼
Web Server Detected?
   │
   ├── No ───────────────► Generate Reports
   │
   ▼ Yes
Run WhatWeb
   │
   ▼
Run Gobuster
   │
   ▼
Run Nikto
   │
   ▼
CVE Lookup
   │
   ▼
Vulnerability Analysis
   │
   ▼
Risk Analysis
   │
   ▼
Generate JSON Report
   │
   ▼
Generate HTML Report
   │
   ▼
Generate PDF Report
   │
   ▼
Display Results
   │
   ▼
End
```

---

## Workflow Summary

1. The user provides a target IP address or domain.
2. ReconX performs an Nmap scan to identify open ports and services.
3. The XML scan results are parsed.
4. The operating system is identified.
5. DNS and WHOIS information is collected.
6. If a web server is detected, ReconX automatically performs:
   - WhatWeb technology detection
   - Gobuster directory enumeration
   - Nikto vulnerability scanning
7. CVE information is collected for detected services.
8. Vulnerabilities are analyzed and assigned a risk level.
9. JSON, HTML, and PDF reports are generated.
10. The results are displayed in the terminal and logged.

---

## Project Structure

```text
ReconX/
│
├── modules/
│   ├── analyzer.py
│   ├── cve_lookup.py
│   ├── display.py
│   ├── dns_enum.py
│   ├── gobuster_parser.py
│   ├── gobusterscanner.py
│   ├── html_report.py
│   ├── logger.py
│   ├── nikto_parser.py
│   ├── os_detection.py
│   ├── parser.py
│   ├── pdf_report.py
│   ├── ranking.py
│   ├── report.py
│   ├── risk.py
│   ├── scanner.py
│   ├── utils.py
│   ├── vulnerability.py
│   ├── webscan.py
│   ├── webscanner.py
│   ├── whatweb_parser.py
│   ├── whatwebscanner.py
│   └── whois_lookup.py
│
├── config.py
├── reconx.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

### Project Components

| File/Folder | Description |
|-------------|-------------|
| `reconx.py` | Main entry point of the ReconX framework |
| `config.py` | Stores project configuration settings |
| `modules/` | Contains all functional modules used by ReconX |
| `requirements.txt` | Python package dependencies |
| `README.md` | Project documentation |
| `LICENSE` | Project license information |
| `.gitignore` | Specifies files and folders ignored by Git |

---

## Future Improvements

The following enhancements can be added in future versions of ReconX:

- SSL/TLS Security Analysis
- Shodan API Integration
- VirusTotal API Integration
- Multi-threaded Scanning
- Email Notification System
- Interactive Web Dashboard
- Additional Vulnerability Scanners
- Automatic CVSS Score Calculation
- Scheduled Automated Scans
- Export Reports in Additional Formats

---

## Author

**Muhammad Sannan Azmat**

Cybersecurity Enthusiast

- GitHub: https://github.com/x257sannan
- LinkedIn: https://www.linkedin.com/in/muhammad-sannan-azmat-8bab59341

---

## Repository

GitHub Repository:

**https://github.com/x257sannan/ReconX**

---

## License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more details.

---

## Disclaimer

**ReconX** is developed for educational purposes and authorized security assessments only.

Users must obtain proper authorization before scanning or testing any systems. The developer is not responsible for any misuse of this tool.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star on GitHub!

**Thank you for visiting the ReconX repository.**

</div>

