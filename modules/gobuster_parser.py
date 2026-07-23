import os


def parse_gobuster(report_file):
    """
    Parse Gobuster output and return discovered paths.
    """

    if not os.path.exists(report_file):
        return []

    directories = []

    with open(report_file, "r", encoding="utf-8", errors="ignore") as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            # Skip banner/header lines
            if line.startswith("="):
                continue

            if line.startswith("["):
                continue

            # Extract discovered path
            if line.startswith("/") or line.startswith("."):

                path = line.split()[0]

                if path not in directories:
                    directories.append(path)

    return directories
