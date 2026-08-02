from rich.console import Console
from rich.panel import Panel

console = Console()

def show_banner():
    banner = r"""
███████╗████████╗ ██████╗
██╔════╝╚══██╔══╝██╔════╝
█████╗     ██║   ██║
██╔══╝     ██║   ██║
██║        ██║   ╚██████╗
╚═╝        ╚═╝    ╚═════╝

        FTC OSINT
"""

    console.print(
        Panel.fit(
            banner,
            title="Version 1.0",
            border_style="red"
        )
    )