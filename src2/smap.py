import sys
import time
import subprocess
import colours as c
from map import NmapHandler
from rich import print as rprint
from rich.panel import Panel 
from rich.console import Console
def load():
    time.sleep(7.25)

def main():
    time.sleep(1)
    rprint(Panel("\n[bold]Advanced Nmap Scans Made Simple and Easy to Use. Save Time Spent Typing Long Nmap Commands. \n", title="[cyan][bold]SimpleMAP", subtitle="[red]Created by Cykro. [bold]Release 1.0.2"))
    time.sleep(1.25)
    print("\n")

    print("Type 'help' for a List of Commands.")

from help import helptable
from map import NmapHandler 
def nmapscripts():
    while True:
        nmap_handler = NmapHandler()
        command = input(f"{c.BOLD}{c.GREEN}SimpleMap-1.0.2-#:{c.RESET} ").strip()

        if command.lower() in ('exit', 'quit'):
            time.sleep(0.5)
            print(f"\n{c.BOLD}{c.CYAN}Exiting Smap Shell.{c.RESET}")
            time.sleep(1)
            break

        elif command.lower() == 'help':
            print(helptable())
        elif command.startswith("vulnscan "):
            target = command.split(" ", 1)[1]
            print("\nScanning... Please wait..\n") #animate loading dots
            nmap_handler.vulnassess_scan(target)

        elif command.startswith("basic "):
            target = command.split(" ", 1)[1]
            print("\nScanning... Please wait..\n")
            nmap_handler.silent_scan(target)

        elif command.startswith("UDP "):
            target = command.split(" ", 1)[1]
            print("\nScanning... Please wait..\n")
            nmap_handler.udp_scan(target)

        elif command.startswith("FIN "):
            target = command.split(" ", 1)[1]
            print("\n")
            nmap_handler.udp_scan(target)

        elif command.startswith("XMAS "):
            target = command.split(" ", 1)[1]
            print("\n")
            nmap_handler.xmas_scan(target)

        elif command.startswith("silentvuln "):
            target = command.split(" ", 1)[1]
            print("\n")
            nmap_handler.silent_vulnscan(target)

        elif command.startswith("OS "):
            target = command.split(" ", 1)[1]
            print("\n")
            nmap_handler.service_os_scan(target)
        else:
            time.sleep(1)
            print(f"\n{c.RED}{c.BOLD}Unknown command. Type 'help' for a list of commands.{c.RESET}\n")


 

if __name__ == "__main__":
    subprocess.run('clear')
    console = Console() 
    with console.status(

    "Loading SimpleMap. ", spinner="material"

):
        load()
    
    main()
    nmapscripts()
    
