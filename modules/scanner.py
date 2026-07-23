import subprocess
import os

def run_nmap(target, start_port, end_port):

    os.makedirs("scans", exist_ok=True)

    output_file = f"scans/{target}.xml"

    command = [
    "nmap",
    "-sV",
    "-O",
    "-Pn",
    "-T4",
    f"-p{start_port}-{end_port}",
    "-oX",
    output_file,
    target
    ]

    process = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    return (
        process.returncode,
        output_file,
        process.stdout,
        process.stderr
    )
