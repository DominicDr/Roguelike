import pyfiglet
from colorama import Fore, Back, Style 


champs = {
    "Warrior": {
        'name': 'Warrior',
        'description': 'Strong, well-built man. He is full of ligth and courage.',
        'health': 100,
        'power': 15,
        'symbol': """
               /\\
               ||____________________
        [00000]||___________________/
               ||
               \/
        """,
    },
    'Troll': {
        'name': 'Troll',
        'description': 'Big monster, living in mountains. He\'s pretty stupid , but really tough.',
        'health': 120,
        'power': 5,
        'symbol': """
                        ___
         ___ __________|###|
        |___|__________|###|
                       |###|
                        \_/
        """,

    },
    'Assassin': {
        'name': 'Assassin',
        'description': 'Fast, silent, master of killing. He has a lot of damage, but he is also weak',
        'health': 80,
        'power': 25,
        'symbol': """
             _
            /
        O===[====================>
            \\_
        """,
    }
}

def print_warrior():
    N = champs['Warrior']['name']
    D = champs['Warrior']['description']
    H = champs['Warrior']['health']
    P = champs['Warrior']['power']
    S = Fore.RED + champs['Warrior']['symbol']
    print(Fore.BLUE + f' Name: {N}')
    print(Fore.BLUE + f' Description: {D}') 
    print(Fore.BLUE + f' Health: {H}')
    print(Fore.BLUE + f' Attack damage: {P}')
    print(S)

def print_troll():
    N = champs['Troll']['name']
    D = champs['Troll']['description']
    H = champs['Troll']['health']
    P = champs['Troll']['power']
    S = Fore.RED + champs['Troll']['symbol']
    print(Fore.BLUE + f' Name: {N}')
    print(Fore.BLUE + f' Description: {D}') 
    print(Fore.BLUE + f' Health: {H}')
    print(Fore.BLUE + f' Attack damage: {P}')
    print(S)


def print_assassin():
    N = champs['Assassin']['name']
    D = champs['Assassin']['description']
    H = champs['Assassin']['health']
    P = champs['Assassin']['power']
    S = Fore.RED + champs['Assassin']['symbol']
    print(Fore.BLUE + f' Name: {N}')
    print(Fore.BLUE + f' Description: {D}') 
    print(Fore.BLUE + f' Health: {H}')
    print(Fore.BLUE + f' Attack damage: {P}')
    print(S)

        
def display_optional_characters():
    line = Fore.YELLOW + '*' * 100 + Style.RESET_ALL
    print_warrior()
    print(line)
    print_troll()
    print(line)
    print_assassin()

def choose_a_character():
    display_title = pyfiglet.figlet_format("CHOOSE YOUR CHARACTER")
    print(Fore.RED + display_title + Style.RESET_ALL)
    display_optional_characters()
