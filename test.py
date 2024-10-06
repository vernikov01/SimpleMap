import sys
from networkenum import NmapHandler
import time
import subprocess
import colours as c
from basics import run_basics
from rich import print
from rich.panel import Panel
from rich.layout import Layout
from rich import *

def main():
    header = Panel("\n[bold]Advanced Nmap Scans Made Simple and Easy to Use. Save Time Spent Typing Long Nmap Commands.", title="[cyan][bold]SimpleMAP", subtitle="[red]Created by Cykro. [bold]Release 1.0.2", height=4)
    print(header)

if __name__ == "__main__":
    time.sleep(1.5)
    main()