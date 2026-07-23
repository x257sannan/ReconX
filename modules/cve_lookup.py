import requests


NVD_API = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def search_cve(product, version):

    query = f"{product} {version}"

    params = {
        "keywordSearch": query,
        "resultsPerPage": 5
    }


    try:

        response = requests.get(
            NVD_API,
            params=params,
            timeout=10
        )


        data = response.json()


        vulnerabilities = []


        for item in data.get("vulnerabilities", []):

            cve = item["cve"]


            cve_id = cve["id"]


            description = (
                cve["descriptions"][0]["value"]
            )


            severity = "UNKNOWN"
            cvss = "N/A"


            metrics = cve.get("metrics", {})


            if "cvssMetricV31" in metrics:

                cvss_data = (
                    metrics["cvssMetricV31"][0]
                    ["cvssData"]
                )

                severity = cvss_data["baseSeverity"]

                cvss = cvss_data["baseScore"]



            vulnerabilities.append({

                "cve": cve_id,

                "severity": severity,

                "cvss": cvss,

                "description": description

            })


        return vulnerabilities


    except Exception as e:

        print(
            f"CVE lookup error: {e}"
        )

        return []
