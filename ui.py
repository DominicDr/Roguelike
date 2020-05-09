from colorama import Fore, Back, Style



def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    color_scheme = {
        0: Back.BLACK + ' ', 
        1: Fore.RED + Back.RED + '|' + Style.RESET_ALL,
        2: Fore.BLUE + Back.BLUE + '.' + Style.RESET_ALL,
        3: Fore.YELLOW + Back.BLACK + '>' + Style.RESET_ALL, 
        4: Fore.LIGHTRED_EX + Back.LIGHTRED_EX + '+' + Style.RESET_ALL,
        5: Fore.GREEN + Back.GREEN + ':' + Style.RESET_ALL,
        6: Fore.MAGENTA + Back.MAGENTA + '#' + Style.RESET_ALL,
        7: Fore.YELLOW + Back.YELLOW + '^' + Style.RESET_ALL,
        8: Fore.LIGHTCYAN_EX + Back.LIGHTCYAN_EX + '~' + Style.RESET_ALL,
        9: Fore.LIGHTMAGENTA_EX + Back.LIGHTMAGENTA_EX + '$' + Style.RESET_ALL,
    }

    for row in board:
        for cell in row:
            if isinstance(cell, str):
                print(cell, end='')
            else:
                print(color_scheme[cell], end='')
        print()
    print()
