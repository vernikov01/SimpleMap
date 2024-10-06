import subprocess
from rich import print as rprint
from rich.layout import Layout
from help import helptable

class NmapHandler:

    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    BOLD = "\033[1m"

    def execute_command(self, command):
        args = command.split()
        try:
            
            result = subprocess.call(['nmap'] + args, text=True)
            if result.returncode != 0:
                print(f"Error executing command make sure command is correct: {result.stderr}")
            else:
                print(result.stdout)
        except Exception as e:
            print(f"Error executing command: {e}")

    def get_help(self):
        helptable()

      
    def advanced_scan(self, target):
        command = f"-A -T2 -O {target}"
        self.execute_command(command)

    def silent_scan(self, target): # make mention of timeframes 
        command = f"-sV -sT -Pn {target}" 
        self.execute_command(command)

    def silent_vulnscan(self, target):
        command = f"-sV -sT -Pn --script vuln {target}"
        self.execute_command(command)

    def udp_scan(self, target):
        command = f"-sU -p- --randomize-hosts {target}" #implement as UDP
        self.execute_command(command)

    def fin_scan(self, target):
        command = f"-sF -T2 -p- --randomize-hosts {target}" #implement as FIN
        self.execute_command(command)

    def null_scan(self, target):
        command = f"-sN -T2 -p- --randomize-hosts {target}" #implement as NULL
        self.execute_command(command)

    def xmas_scan(self, target):
        command = f"-sX -T2 -p- --randomize-hosts {target}" #implement as XMAS
        self.execute_command(command)

    def vulnassess_scan(self, target):
        command = f"-sV -sC -p- --randomize-hosts {target}" #implement vulncheck
        self.execute_command(command)

    def service_os_scan(self, target):
        command = f"-sV -O -p- --randomize-hosts {target}" #implement serviceos
        self.execute_command(command)
