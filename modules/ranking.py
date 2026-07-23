def rank_vulnerabilities(vulnerabilities):

    severity_order = {
        "CRITICAL": 4,
        "HIGH": 3,
        "MEDIUM": 2,
        "LOW": 1,
        "UNKNOWN": 0
    }


    for vuln in vulnerabilities:

        severity = vuln.get(
            "severity",
            "UNKNOWN"
        ).upper()

        vuln["priority"] = severity_order.get(
            severity,
            0
        )


    ranked = sorted(
        vulnerabilities,
        key=lambda x: (
            x.get("priority",0),
            float(x.get("cvss",0))
            if str(x.get("cvss","0")).replace(".","").isdigit()
            else 0
        ),
        reverse=True
    )


    return ranked
