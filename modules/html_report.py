import os

def generate_html(report):
    os.makedirs("reports", exist_ok=True)

    html_file = "reports/report.html"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>AutoReconX Report</title>
    <style>
    body {{
        font-family: Arial;
        background:#f4f4f4;
        margin:40px;
    }}
    .container {{
        background:white;
        padding:20px;
        border-radius:10px;
    }}
    h1 {{ color:#0d6efd; }}
    table {{ width:100%; border-collapse:collapse; }}
    th {{ background:#0d6efd; color:white; padding:10px; }}
    td {{ border:1px solid #ddd; padding:8px; }}
    .high {{ color:red; }}
    .medium {{ color:orange; }}
    .low {{ color:green; }}
    .info {{ color:blue; }}
    </style>
    </head>
    <body>
    <div class="container">
    <h1>AutoReconX Scan Report</h1>

    <h2>Target Information</h2>
    <ul>
    <li><b>Target IP:</b> {report.get("ip","Unknown")}</li>
    <li><b>Operating System:</b> {report.get("os","Unknown")}</li>
    </ul>

    <h2>Open Ports</h2>
    <table>
    <tr><th>Port</th><th>Protocol</th><th>Service</th><th>Product</th><th>Version</th></tr>
    """

    for port in report.get("ports", []):
        html += f"""
        <tr>
        <td>{port.get("port","")}</td>
        <td>{port.get("protocol","")}</td>
        <td>{port.get("service","")}</td>
        <td>{port.get("product","")}</td>
        <td>{port.get("version","")}</td>
        </tr>
        """

    html += "</table>"

    if "technologies" in report:
        html += "<h2>Detected Technologies</h2><ul>"
        for tech in report["technologies"]:
            html += f"<li>{tech}</li>"
        html += "</ul>"

    if "directories" in report:
        html += "<h2>Directories</h2><ul>"
        for directory in report["directories"]:
            html += f"<li>{directory}</li>"
        html += "</ul>"

    if "nikto_findings" in report:
        html += "<h2>Nikto Findings</h2><ul>"
        for finding in report["nikto_findings"]:
            html += f"<li>{finding}</li>"
        html += "</ul>"

    # Vulnerability Analysis Table
    if "vulnerabilities" in report:
        html += """
        <h2>Vulnerability Analysis</h2>
        <table>
        <tr><th>Severity</th><th>Details</th></tr>
        """
        for vuln in report["vulnerabilities"]:
            severity = vuln.get("severity","info").lower()
            details = vuln.get("description") or vuln.get("issue") or vuln.get("cve","N/A")
            html += f"""
            <tr>
            <td class="{severity}">{vuln.get("severity","Unknown")}</td>
            <td>{details}</td>
            </tr>
            """
        html += "</table>"

    # Extra vulnerability section
    vulnerabilities = report.get("vulnerabilities", [])
    if vulnerabilities:
        html += "<h2>Vulnerability Findings</h2>"
        for vuln in vulnerabilities:
            html += f"""
            <div>
            <h3>{vuln.get('cve','N/A')}</h3>
            <p><b>Service:</b> {vuln.get('service','Unknown')}</p>
            <p><b>Severity:</b> {vuln.get('severity','Unknown')}</p>
            <p><b>CVSS Score:</b> {vuln.get('cvss','N/A')}</p>
            <p><b>Description:</b> {vuln.get('description', vuln.get('issue','No description'))}</p>
            <p><b>Recommendation:</b> Apply security patches and update the affected software.</p>
            </div>
            <hr>
            """
    else:
        html += "<h2>Vulnerability Findings</h2><p>No vulnerabilities detected.</p>"

    html += """
    </div>
    </body>
    </html>
    """

    with open(html_file, "w") as file:
        file.write(html)

    return html_file
