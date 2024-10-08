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
        elif command.startswith("vulnscan "):
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

        elif command.startswith("udp "):
            target = command.split(" ", 1)[1]
            print("\n")
            nmap_handler.execute_command(f"-sU -p- --randomize-hosts {target}")

        elif command.startswith("fin "):
            target = command.split(" ", 1)[1]
            print("\nScanning... Please wait..\n")
            nmap_handler.fin_scan(target)

        else:
            time.sleep(1)
            print(f"\n{c.RED}{c.BOLD}Unknown command. Type 'help' for a list of commands.{c.RESET}\n")
