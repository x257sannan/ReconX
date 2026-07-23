import subprocess
import os


def run_nikto(target):

    os.makedirs("web_reports", exist_ok=True)

    output_file = f"web_reports/{target}_nikto.txt"

    command = [
        "nikto",
        "-h",
        target,
        "-output",
        output_file
    ]

    print("\n")
    print("=" * 60)
    print("Starting Nikto Web Scan")
    print("=" * 60)

    result = subprocess.run(command)

    return result.returncode, output_file
