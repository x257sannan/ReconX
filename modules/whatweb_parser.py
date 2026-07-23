import os


def parse_whatweb(report_file):

    if not os.path.exists(report_file):
        return {}

    with open(report_file, "r", encoding="utf-8", errors="ignore") as f:
        data = f.read()

    result = {
        "server": "Unknown",
        "os": "Unknown",
        "technologies": []
    }

    if "Apache[" in data:
        start = data.find("Apache[") + 7
        end = data.find("]", start)
        result["server"] = "Apache " + data[start:end]

    if "Ubuntu Linux" in data:
        result["os"] = "Ubuntu Linux"

    if "HTML5" in data:
        result["technologies"].append("HTML5")

    if "Google-Analytics" in data:
        result["technologies"].append("Google Analytics")

    if "PHP" in data:
        result["technologies"].append("PHP")

    return result
