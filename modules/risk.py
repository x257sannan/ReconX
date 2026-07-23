from rich.console import Console
from rich.panel import Panel

console = Console()


def show_risk_dashboard(vulnerabilities):
    high = 0
    medium = 0
    low = 0
    info = 0

    for vuln in vulnerabilities:
        severity = vuln.get("severity", "").lower()

        if severity == "high":
            high += 1
        elif severity == "medium":
            medium += 1
        elif severity == "low":
            low += 1
        else:
            info += 1

    if high > 0:
        overall = "[bold red]HIGH[/bold red]"
    elif medium > 0:
        overall = "[bold yellow]MEDIUM[/bold yellow]"
    elif low > 0:
        overall = "[bold green]LOW[/bold green]"
    else:
        overall = "[bold cyan]INFO[/bold cyan]"

    dashboard = f"""
🔴 High      : {high}

🟡 Medium    : {medium}

🟢 Low       : {low}

🔵 Info      : {info}

Overall Risk : {overall}
"""

    console.print(
        Panel(
            dashboard,
            title="[bold red]Risk Assessment[/bold red]",
            border_style="red"
        )
    )
def calculate_risk_summary(vulnerabilities):

    high = 0
    medium = 0
    low = 0
    info = 0


    for vuln in vulnerabilities:

        severity = vuln.get("severity", "").lower()

        if severity == "high":
            high += 1

        elif severity == "medium":
            medium += 1

        elif severity == "low":
            low += 1

        else:
            info += 1


    # Calculate risk score

    score = (
        (high * 10) +
        (medium * 5) +
        (low * 2)
    )


    # Determine severity

    if high > 0 or score >= 50:
        overall = "HIGH"

    elif medium > 0 or score >= 20:
        overall = "MEDIUM"

    elif low > 0:
        overall = "LOW"

    else:
        overall = "INFO"


    return {

        "high": high,

        "medium": medium,

        "low": low,

        "info": info,

        "score": score,

        "severity": overall

    }
