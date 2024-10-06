import sys
import time
import subprocess
import colours as c
from rich import print as rprint
from rich.panel import Panel
from rich.layout import Layout
from rich import *
from rich.console import Console
from rich.table import Table

def helptable():

    table = Table(title="Help Menu")

    table.add_column("[bold] Command ", style="white", no_wrap=True)
    table.add_column("[bold] Scan Description ", style="white")
    table.add_column("[bold] Scan Speed ", justify="right", style="white")
    table.add_column("[bold] Scan ETA", justify="right", style="white")

    table.add_row("PING", "Simple Ping Request for checking if ip responds", "[green][bold]Fastest", "2-15 sec", end_section=True)
    table.add_row("BASIC", "Standard Nmap Scan", "[green]Fast", "1-10 mins", end_section=True)
    table.add_row("UDP", "Scans for any open ports using UDP", "[yellow][bold]Normal", "5-30 mins", end_section=True)
    table.add_row("FIN", "FIN FireWall Bypass Scan", "[bold][red]Slow", "N/A", end_section=True)
    table.add_row("NULL", "NULL Firewall Bypass Scan", "[bold][red]Slow", "N/A", end_section=True)
    table.add_row("XMAS", "XMAS Firewall Bypass Scan", "[bold][red]Slow", "N/A", end_section=True)
    table.add_row("SILENTVULN", "Stealthy Vulnerability Scan", "[bold][red]Slow", "5-45 mins", end_section=True)
    table.add_row("OS", "Loud but fast scan to obtain the Operating System", "[green]Fast", "5-15 mins", end_section=True)
    table.add_row("[bold](command)", "[bold](Description)", "[bold](speed)", "[bold](ETA mins)", end_section=True)





    console = Console()
    console.print(table)
