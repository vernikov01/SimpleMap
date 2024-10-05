import subprocess
import sys
from networkenum import NmapHandler
import colours as c
import time 



while True:
    nmap_handler = NmapHandler()
    command = input(f"{c.BOLD}{c.GREEN}SimpleMap-#:{c.RESET} ").strip()

    if command.lower() in ('exit', 'quit'):
        time.sleep(0.5)
        print(f"\n{c.BOLD}{c.CYAN}Exiting Smap Shell.{c.RESET}")
        time.sleep(1)
        break

    elif command.lower() == 'help':
        print(nmap_handler.get_help())
    elif command.startswith("advanced "):
        target = command.split(" ", 1)[1]
        print("\nScanning... Please wait..\n")
        nmap_handler.advanced_scan(target)

    elif command.startswith("silent "):
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
        nmap_handler.execute_command(f"-sP {target}")
    else:
        time.sleep(1)
        print(f"\n{c.RED}{c.BOLD}Unknown command. Type 'help' for a list of commands.{c.RESET}\n")