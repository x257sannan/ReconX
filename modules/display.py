from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def display_results(report):

    # -------------------------------------------------
    # Scan Results Table
    # -------------------------------------------------

    table = Table(title="AutoReconX Scan Results")

    table.add_column("Port", style="cyan", justify="center")
    table.add_column("Protocol", style="green", justify="center")
    table.add_column("Service", style="yellow")
    table.add_column("Product", style="magenta")
    table.add_column("Version", style="white")

    for port in report["ports"]:

        table.add_row(
            port["port"],
            port["protocol"],
            port["service"],
            port["product"],
            port["version"]
        )

    console.print(table)

    # -------------------------------------------------
    # Network Summary
    # -------------------------------------------------

    services = sorted(set(port["service"] for port in report["ports"]))
    protocols = sorted(set(port["protocol"] for port in report["ports"]))

    summary = f"""
[bold cyan]Target Information[/bold cyan]
────────────────────────────────────────

Target IP          : {report['ip']}
Operating System   : {report['os']}


[bold cyan]Network Summary[/bold cyan]
────────────────────────────────────────

Open Ports         : {len(report['ports'])}
Services           : {", ".join(services)}
Protocols          : {", ".join(protocols)}


[bold cyan]Web Scan Status[/bold cyan]
────────────────────────────────────────

WhatWeb            : {'Completed' if 'whatweb_report' in report else 'Not Executed'}

Nikto              : {'Completed' if 'nikto_report' in report else 'Not Executed'}

Gobuster           : {'Completed' if 'gobuster_report' in report else 'Not Executed'}

[bold cyan]Reports Generated[/bold cyan]
────────────────────────────────────────

✔ XML Report

✔ JSON Report

✔ CSV Report

✔ WhatWeb Report

✔ Nikto Report
"""

    console.print(
        Panel(
            summary,
            title="[bold green]AutoReconX Dashboard[/bold green]",
            border_style="green"
        )
    )
