from colorama import Fore, Back, Style



def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    color_scheme = {
        0: Back.BLACK + ' ', 
        1: Fore.LIGHTMAGENTA_EX + Back.RED + '|' + Style.RESET_ALL,
        2: Fore.LIGHTCYAN_EX + Back.BLUE + '.' + Style.RESET_ALL,
        3: Fore.YELLOW + Back.BLACK + '>' + Style.RESET_ALL, 
        4: Fore.RED + Back.LIGHTRED_EX + '+' + Style.RESET_ALL,
        5: Fore.LIGHTCYAN_EX + Back.GREEN + ':' + Style.RESET_ALL,
        6: Fore.LIGHTMAGENTA_EX + Back.MAGENTA + '#' + Style.RESET_ALL,
        7: Fore.BLACK + Back.YELLOW + '^' + Style.RESET_ALL,
        8: Fore.GREEN + Back.LIGHTCYAN_EX + '~' + Style.RESET_ALL,
        9: Fore.MAGENTA + Back.LIGHTMAGENTA_EX + '$' + Style.RESET_ALL,
    }

    for row in board:
        for cell in row:
            if isinstance(cell, str):
                print(cell, end='')
            else:
                print(color_scheme[cell], end='')
        print()
    print()
