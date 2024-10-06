import time 
from rich.console import Console

def waiting():
    time.sleep(10)


console = Console()

with console.status(

    "Please wait - solving global problems...", spinner="dots"

): 
    waiting()