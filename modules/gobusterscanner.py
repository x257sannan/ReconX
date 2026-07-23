import subprocess
import os


def run_gobuster(target):

    os.makedirs("web_reports", exist_ok=True)

    output_file = f"web_reports/{target}_gobuster.txt"

    wordlist = "/usr/share/wordlists/dirb/common.txt"

    command = [
        "gobuster",
        "dir",
        "-u",
        f"http://{target}",
        "-w",
        wordlist,
        "-o",
        output_file
    ]

    print("\n")
    print("=" * 60)
    print("Starting Gobuster Directory Scan")
    print("=" * 60)

    result = subprocess.run(command)

    return result.returncode, output_file
