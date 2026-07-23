import subprocess
import os


def run_whatweb(target):

    os.makedirs("web_reports", exist_ok=True)

    output_file = f"web_reports/{target}_whatweb.txt"

    command = [
        "whatweb",
        target,
        "--log-brief",
        output_file
    ]

    print("\n")
    print("=" * 60)
    print("Starting WhatWeb Technology Detection")
    print("=" * 60)

    result = subprocess.run(command)

    return result.returncode, output_file
