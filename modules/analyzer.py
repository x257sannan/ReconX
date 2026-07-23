def analyze(report):

    vulnerabilities = []

    # ------------------------------------
    # OS Analysis
    # ------------------------------------

    os_name = report.get("os", "")

    if "Linux" in os_name:
        vulnerabilities.append({
            "severity": "Info",
            "issue": "Linux Host Detected"
        })

    # ------------------------------------
    # Open Ports
    # ------------------------------------

    for port in report.get("ports", []):

        service = port["service"]

        if service == "ftp":
            vulnerabilities.append({
                "severity": "High",
                "issue": "FTP service detected"
            })

        elif service == "telnet":
            vulnerabilities.append({
                "severity": "Critical",
                "issue": "Telnet service detected"
            })

        elif service == "ssh":
            vulnerabilities.append({
                "severity": "Low",
                "issue": "SSH service detected"
            })

        elif service == "http":
            vulnerabilities.append({
                "severity": "Info",
                "issue": "Web Server Detected"
            })

    # ------------------------------------
    # Nikto Findings
    # ------------------------------------

    for finding in report.get("nikto_findings", []):

        if "Apache version is outdated" in finding:

            vulnerabilities.append({
                "severity": "High",
                "issue": finding
            })

        elif "Missing" in finding:

            vulnerabilities.append({
                "severity": "Medium",
                "issue": finding
            })

        else:

            vulnerabilities.append({
                "severity": "Info",
                "issue": finding
            })

    return vulnerabilities
