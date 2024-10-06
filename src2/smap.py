import sys
import time
import subprocess
import colours as c
from map import NmapHandler
from rich import print as rprint
from rich.panel import Panel


def main():
    time.sleep(1)
    rprint(Panel("\n[bold]Advanced Nmap Scans Made Simple and Easy to Use. Save Time Spent Typing Long Nmap Commands. \n", title="[cyan][bold]SimpleMAP", subtitle="[red]Created by Cykro. [bold]Release 1.0.2"))
    time.sleep(1.25)
    print("\n")

import colours as c
import time 
from help import helptable
from map import NmapHandler 
def nmapscripts():
    while True:
        nmap_handler = NmapHandler()
        command = input(f"{c.BOLD}{c.GREEN}SimpleMap-#:{c.RESET} ").strip()

        if command.lower() in ('exit', 'quit'):
            time.sleep(0.5)
            print(f"\n{c.BOLD}{c.CYAN}Exiting Smap Shell.{c.RESET}")
            time.sleep(1)
            break

        elif command.lower() == 'help':
            print(helptable())
        elif command.startswith("silentvuln "):
            target = command.split(" ", 1)[1]
            print("\nScanning... Please wait..\n") #animate this
            nmap_handler.vulnassess_scan(target)

        elif command.startswith("basic "):
            target = command.split(" ", 1)[1]
            print("\nScanning... Please wait..\n")
            nmap_handler.silent_scan(target)

        elif command.startswith("silentvuln "):
            target = command.split(" ", 1)[1]
            print("\nScanning... Please wait..\n")
            nmap_handler.silent_vulnscan(target)

        elif command.startswith("ping "):
            target = command.split(" ", 1)[1]
            print("\n")
            nmap_handler.execute_command(f"-A T2 -O --script=default --randomize-hosts {target}")

        elif command.startswith("ping "):
            target = command.split(" ", 1)[1]
            print("\n")
            nmap_handler.execute_command(f"{target}")

        else:
            time.sleep(1)
            print(f"\n{c.RED}{c.BOLD}Unknown command. Type 'help' for a list of commands.{c.RESET}\n")


    

if __name__ == "__main__":
    subprocess.run('clear')
    main()
    nmapscripts()
    
