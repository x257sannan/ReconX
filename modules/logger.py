from rich.console import Console
from rich.logging import RichHandler
import logging
import os

console = Console()

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        RichHandler(console=console),
        logging.FileHandler("logs/reconx.log")
    ]
)

logger = logging.getLogger("ReconX")
