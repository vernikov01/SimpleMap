import sys
from networkenum import NmapHandler
import time
import subprocess
import colours as c

def main():
    print(f"\n{c.CYAN}{c.BOLD}Welcome to Smap! Nmap Made Simple! \n\n {c.RESET}{c.BLUE}Type 'help' for commands.\n{c.RESET}")
    time.sleep(1.25)
    subprocess.run(['python3', 'src/basics.py'])
    

if __name__ == "__main__":
    subprocess.run('clear')
    main()
