import os


def parse_nikto(report_file):
    """
    Parse Nikto report and extract important findings.
    """

    if not os.path.exists(report_file):
        return []

    findings = []

    with open(report_file, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    for line in lines:

        line = line.strip()

        # Ignore empty lines
        if not line:
            continue

        # Apache Outdated
        if "appears to be outdated" in line:
            findings.append("Apache version is outdated")

        # Missing Security Headers
        elif "content-security-policy" in line.lower():
            findings.append("Missing Content-Security-Policy")

        elif "strict-transport-security" in line.lower():
            findings.append("Missing HSTS")

        elif "x-content-type-options" in line.lower():
            findings.append("Missing X-Content-Type-Options")

        elif "permissions-policy" in line.lower():
            findings.append("Missing Permissions-Policy")

        elif "referrer-policy" in line.lower():
            findings.append("Missing Referrer-Policy")

        # HTTP Methods
        elif "Allowed HTTP Methods" in line:
            findings.append("HTTP OPTIONS method enabled")

        # Apache MultiViews
        elif "mod_negotiation" in line:
            findings.append("Apache MultiViews Enabled")

        # Uncommon Header
        elif "Uncommon header" in line:
            findings.append("Uncommon HTTP Header Detected")

    # Remove duplicates while preserving order
    unique_findings = []

    for item in findings:
        if item not in unique_findings:
            unique_findings.append(item)

    return unique_findings
