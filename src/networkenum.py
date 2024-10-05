import subprocess

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
            
            result = subprocess.run(['nmap'] + args, capture_output=True, text=True )
            if result.returncode != 0:
                print(f"Error executing command: {result.stderr}")
            else:
                print(result.stdout)
        except Exception as e:
            print(f"Error executing command: {e}")

    def get_help(self):
        return f"""
{self.BOLD}{self.CYAN}Available Commands:{self.RESET}

+-------------------------------------------------------------------------------+
|{self.GREEN} {self.BOLD} scan {self.RESET}<target>       {self.YELLOW}Perform a basic scan on the target.{self.RESET}
+-------------------------------------------------------------------------------+
|{self.GREEN} {self.BOLD} advanced {self.RESET}<target>   {self.YELLOW}Perform an advanced but aggressive scan.{self.RESET}
+-------------------------------------------------------------------------------+
|{self.GREEN} {self.BOLD} silent {self.RESET}<target>     {self.YELLOW}Perform a quiet scan, which can take longer.{self.RESET}
+-------------------------------------------------------------------------------+
|{self.GREEN} {self.BOLD} silentvuln {self.RESET}<target> {self.YELLOW}Perform a quiet scan which checks for vulnerabilities.{self.RESET}
+-------------------------------------------------------------------------------+
|{self.GREEN} {self.BOLD} ping {self.RESET}<target>       {self.YELLOW}Check to see if the target IP is responsive.{self.RESET}
+-------------------------------------------------------------------------------+

+-------------------------------------------------------------------------------+
|{self.GREEN} {self.BOLD} help {self.RESET}                       {self.YELLOW}Show this help message.{self.RESET}
+-------------------------------------------------------------------------------+
|{self.GREEN} {self.BOLD} exit {self.RESET}                       {self.YELLOW}Exit the smap shell.{self.RESET}
+-------------------------------------------------------------------------------+  
    """
    def advanced_scan(self, target):
        command = f"-A -T2 -sV {target}"
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
        command = f"-sF -p- --randomize-hosts {target}" #implement as FIN
        self.execute_command(command)

    def null_scan(self, target):
        command = f"-sN -p- --randomize-hosts {target}" #implement as NULL
        self.execute_command(command)

    def xmas_scan(self, target):
        command = f"-sX -p- --randomize-hosts {target}" #implement as XMAS
        self.execute_command(command)

    def vulnassess_scan(self, target):
        command = f"-sV -sC -p- --randomize-hosts {target}" #implement vulncheck
        self.execute_command(command)

    def service_os_scan(self, target):
        command = f"-sV -O -p- --randomize-hosts {target}" #implement serviceos
        self.execute_command(command)
