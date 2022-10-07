import random
from colorama import Fore, Style
def deff():
    x = input(f"Nochmal? {Fore.GREEN}(J) Ja{Style.RESET_ALL} oder {Fore.RED}(N) Nein{Style.RESET_ALL} :")
    if x == "j" or "J":
        gluck()
    if x == "n" or "N":
        exit()

def gluck():
    var = random.randint(1, 100)
    print(var)
    if var == 100:
        print(f"{Fore.GREEN}VOLLE PUNKTZAHL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{Style.RESET_ALL}") 
    if var == 50:
        print(f"{Fore.YELLOW}HALBE PUNKTZAHL!{Style.RESET_ALL}")
    if var == 25:
        print(f"{Fore.YELLOW}VIERTEL PUNKTZAHL{Style.RESET_ALL}")
    if var == 75:
        print(f"{Fore.GREEN}DREIVIERTEL PUNKTZAHL!{Style.RESET_ALL}")
    if var == 69:
        print(f"{Fore.LIGHTCYAN_EX}DER WAHRE GEWINN!{Style.RESET_ALL}")
    deff()
gluck()