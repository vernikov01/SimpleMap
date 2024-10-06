import sys
import time
import subprocess
import colours as c
from basics import run_basics
from rich import print as rprint
from rich.panel import Panel
from helpmenu import helptable


def main():
    time.sleep(1)
    rprint(Panel("\n[bold]Advanced Nmap Scans Made Simple and Easy to Use. Save Time Spent Typing Long Nmap Commands. \n", title="[cyan][bold]SimpleMAP", subtitle="[red]Created by Cykro. [bold]Release 1.0.2"))
    time.sleep(1.25)
    print("\n")

    

if __name__ == "__main__":
    subprocess.run('clear')
    main()
    run_basics()
