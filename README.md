# ReconX – Automated Reconnaissance Framework

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## Overview

ReconX is an automated reconnaissance framework developed in Python to simplify and accelerate the information gathering phase of penetration testing. It combines multiple security tools into a single framework, allowing security professionals and students to perform reconnaissance efficiently while generating structured reports.

---

## Objectives

- Automate the reconnaissance phase of penetration testing.
- Reduce manual effort during information gathering.
- Detect network services and web technologies.
- Perform automated vulnerability assessment.
- Generate professional reports for further analysis.

---

## Features

- Network Port Scanning (Nmap)
- Service & Version Detection
- Operating System Detection
- DNS Enumeration
- WHOIS Lookup
- SSL/TLS Analysis
- Web Server Detection
- Nikto Web Vulnerability Scanning
- Gobuster Directory Enumeration
- WhatWeb Technology Detection
- CVE Lookup
- Risk Analysis
- JSON Report Generation
- HTML Report Generation
- PDF Report Generation
- Logging System
- Modular Architecture

---

## Project Structure

```
ReconX/
│
├── reconx.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
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
│   ├── ssl_scan.py
│   ├── utils.py
│   ├── vulnerability.py
│   ├── webscan.py
│   ├── webscanner.py
│   ├── whatweb_parser.py
│   ├── whatwebscanner.py
│   └── whois_lookup.py
│
├── scans/
├── reports/
├── web_reports/
└── logs/
```

---

## Technologies Used

### Programming Language

- Python 3

### External Security Tools

- Nmap
- Nikto
- Gobuster
- WhatWeb
- OpenSSL

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

Clone the repository

```bash
git clone https://github.com/x257sannan/ReconX.git
```

Go to the project directory

```bash
cd ReconX
```

Install the required Python packages

```bash
pip install -r requirements.txt
```

---

## Usage

Basic Scan

```bash
python3 reconx.py <target>
```

Example

```bash
python3 reconx.py scanme.nmap.org
```

---

## Workflow

1. User enters the target.
2. ReconX validates the input.
3. Nmap scans the target.
4. XML results are parsed.
5. Open ports and services are identified.
6. Web services are detected automatically.
7. Additional web reconnaissance is performed.
8. Vulnerability information is collected.
9. Reports are generated.
10. Results are displayed to the user.

---

## Output

ReconX generates:

- Console Output
- JSON Report
- HTML Report
- PDF Report
- Log Files

---

## Screenshots

### Running ReconX

_Add your screenshot here._

### Scan Results

_Add your screenshot here._

### HTML Report

_Add your screenshot here._

### PDF Report

_Add your screenshot here._

---

## Future Improvements

- CVSS Score Integration
- Automated Exploit Recommendation
- Shodan API Integration
- VirusTotal API Integration
- Multi-threaded Scanning
- Email Reporting
- Interactive Dashboard

---

## License

This project is released under the MIT License.

---

## Author

**Muhammad Sannan Azmat**

Cybersecurity Enthusiast

GitHub: https://github.com/x257sannan

LinkedIn: https://www.linkedin.com/in/muhammad-sannan-azmat-8bab59341

---

## Repository

https://github.com/x257sannan/ReconX

---

### Disclaimer

ReconX is intended for educational purposes and authorized security assessments only. Always obtain proper permission before scanning or testing any systems.
