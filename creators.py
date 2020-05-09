import time
import pyfiglet
from colorama import Fore, Back, Style

creators = [
            "Adrian 'Shaman' Pacholarz",
            "and",
            "Dominik 'Drazi' Drazek",

]

def print_creators():
    it_guys = creators
    print(Fore.RED + pyfiglet.figlet_format("Creators:\n", font='doom') + Style.RESET_ALL)
    time.sleep(3)
    for element in it_guys:
        if element == it_guys[1]:
            print(Fore.BLUE + pyfiglet.figlet_format(element.center(60), font='doom') + Style.RESET_ALL)
        else:
            print(Fore.GREEN + pyfiglet.figlet_format(element, font='doom') + Style.RESET_ALL)
        time.sleep(3)
    print(Fore.RED + 'Press any key to back to menu' + Style.RESET_ALL)
        

