from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich import box

from banner import show_banner

console = Console()

VERSION = "1.0.0"

def menu():

    while True:

        console.clear()

        show_banner()

        table = Table(
            title="MAIN MENU",
            box=box.DOUBLE,
            border_style="red"
        )

        table.add_column("Option", style="red", justify="center")
        table.add_column("Module", style="white")

        table.add_row("1", "IP Lookup")
        table.add_row("2", "Phone Lookup")
        table.add_row("3", "Email Lookup")
        table.add_row("4", "Username Search")
        table.add_row("5", "Domain Lookup")
        table.add_row("6", "DNS Lookup")
        table.add_row("7", "Whois")
        table.add_row("8", "Metadata")
        table.add_row("9", "Settings")
        table.add_row("0", "Exit")

        console.print(table)

        choice = Prompt.ask(
            "[red]Choose an option[/red]"
        )

        if choice == "0":
            console.print(
                "\n[green]Goodbye![/green]"
            )
            break

        console.print(
            Panel(
                f"[yellow]Module {choice} coming soon...[/yellow]",
                border_style="red"
            )
        )

        input("\nPress ENTER to continue...")


if __name__ == "__main__":
    menu()