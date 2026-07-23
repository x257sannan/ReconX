#!/usr/bin/env python3

import argparse
import time
import config
import socket

from modules.display import display_results
from modules.report import save_json, save_csv
from modules.logger import logger
from modules.utils import banner
from modules.scanner import run_nmap
from modules.parser import parse_nmap

from modules.webscanner import run_nikto
from modules.whatwebscanner import run_whatweb
from modules.gobusterscanner import run_gobuster
from modules.analyzer import analyze
from modules.risk import show_risk_dashboard, calculate_risk_summary
from modules.html_report import generate_html
from modules.pdf_report import generate_pdf
from modules.vulnerability import check_online_vulnerabilities
from modules.ranking import rank_vulnerabilities
from rich.console import Console 

console = Console()

from modules.whatweb_parser import parse_whatweb
from modules.nikto_parser import parse_nikto
from modules.gobuster_parser import parse_gobuster

from config import *


def main():
    banner()

    parser = argparse.ArgumentParser(
        description="ReconX - Automated Reconnaissance Framework"
    )

    parser.add_argument(
    "--version",
    action="version",
    version="ReconX v1.0"
    )

    parser.add_argument(
        "target",
        help="Target IP Address or Domain"
    )

    parser.add_argument(
        "-m", "--mode",
        choices=["quick", "full", "web"],
        default="quick",
        help="Select scan mode"
    )

    args = parser.parse_args()

    # Set port ranges based on mode
    if args.mode == "quick":
        start = config.QUICK_START_PORT
        end = config.QUICK_END_PORT
    elif args.mode == "full":
        start = config.FULL_START_PORT
        end = config.FULL_END_PORT
    elif args.mode == "web":
        start = config.WEB_START_PORT
        end = config.WEB_END_PORT
    else:
        start, end = DEFAULT_START_PORT, DEFAULT_END_PORT

    start_time = time.time()

    logger.info(f"Target : {args.target}")
    logger.info(f"Ports  : {start}-{end}")

    console.print(
    f"""
    [+] Target : {args.target}
    [+] Mode   : {args.mode}
    [+] Status : Scan Started
     """
  )
    code, xml_file, stdout, stderr = run_nmap(
        args.target,
        start,
        end
    )

    if code == 0:
        logger.info("Scan Completed Successfully")
        logger.info(f"XML Report : {xml_file}")

        report = parse_nmap(xml_file)

        # Vulnerability Analysis (online + ranking)
        vulnerabilities = check_online_vulnerabilities(report.get("ports", []))
        vulnerabilities = rank_vulnerabilities(vulnerabilities)
        report["vulnerabilities"] = vulnerabilities

        # Save XML Report
        report["xml_report"] = xml_file

        # Detect Web Server
        web_detected = any(p["port"] in ["80", "443"] for p in report["ports"])

        if web_detected:
            logger.info("Web Server Detected")

            # WHATWEB
            logger.info("Starting WhatWeb Scan...")
            whatweb_code, whatweb_report = run_whatweb(args.target)
            if whatweb_code == 0:
                logger.info("WhatWeb Scan Completed Successfully")
                logger.info(f"WhatWeb Report : {whatweb_report}")
                report["whatweb_report"] = whatweb_report
                report["technologies"] = parse_whatweb(whatweb_report)
            else:
                logger.error("WhatWeb Scan Failed")

            # NIKTO
            logger.info("Starting Nikto Scan...")
            nikto_code, nikto_report = run_nikto(args.target)
            if nikto_code == 0:
                logger.info("Nikto Scan Completed Successfully")
                logger.info(f"Nikto Report : {nikto_report}")
                report["nikto_report"] = nikto_report
                report["nikto_findings"] = parse_nikto(nikto_report)
            else:
                logger.error("Nikto Scan Failed")

            # GOBUSTER
            logger.info("Starting Gobuster Scan...")
            gobuster_code, gobuster_report = run_gobuster(args.target)
            if gobuster_code == 0:
                logger.info("Gobuster Scan Completed Successfully")
                logger.info(f"Gobuster Report : {gobuster_report}")
                report["gobuster_report"] = gobuster_report
                report["directories"] = parse_gobuster(gobuster_report)
            else:
                logger.error("Gobuster Scan Failed")

        else:
            logger.info("No Web Server Detected")
            logger.info("Skipping WhatWeb, Nikto and Gobuster")

        # Local Vulnerability Analysis
        local_vulns = analyze(report)
        report["local_vulnerabilities"] = local_vulns

        show_risk_dashboard(vulnerabilities)
        risk_summary = calculate_risk_summary(vulnerabilities)
        report["risk"] = risk_summary

        # Display Results
        display_results(report)

        # Save Reports
        save_json(report)
        save_csv(report)

        pdf = generate_pdf(report)
        print(f"[+] PDF Report Generated: {pdf}")

        html_report = generate_html(report)
        logger.info(f"HTML report saved : {html_report}")

        end_time = time.time()
        duration = round(end_time - start_time, 2)

        logger.info(f"Scan Duration : {duration} seconds")
        logger.info("JSON report saved in reports/report.json")
        logger.info("CSV report saved in reports/report.csv")

    else:
        logger.error(stderr)


if __name__ == "__main__":
    main()
