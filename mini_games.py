import random
import time
import pyfiglet
from colorama import Fore, Style
import util

paper = """

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

""" 


scissors = """

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock = """

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

def display_instruction():
    game = ('ROCK, ', 'PAPER, ', 'SCISSORS!')
    for element in game:
        format_element = pyfiglet.figlet_format(element, font='cybermedium')
        print(Fore.BLUE + format_element, end=' ')
    print('You have to win this game to open chest. Let\'s choose a number. Good luck!')
        

def displaying_game():
    names = ['1) Paper', '2) Scisorss', '3) Rock']
    game = (paper, scissors, rock)
    display_instruction()
    time.sleep(5)
    for n, g in zip(names, game): 
        print(Fore.BLUE + n, g + Style.RESET_ALL)

def win():
    win = True
    you_win = pyfiglet.figlet_format('You win!', font='big')
    print(Fore.GREEN + you_win + Style.RESET_ALL)
    time.sleep(3)
    return win

def lost():
    win = False
    you_lost = pyfiglet.figlet_format('You lost!', font='big')
    print(Fore.RED + you_lost + Style.RESET_ALL)
    time.sleep(3)
    return win

def draw():
    draw = pyfiglet.figlet_format('Draw! Bonus round!', font='big')
    print(Fore.YELLOW + draw + Style.RESET_ALL)
    time.sleep(3)

def time_left():
    t = 5
    while t != 0:
        print(t)
        time.sleep(1)
        t -= 1
       

def play_game():
    displaying_game()
    game = (paper, scissors, rock)
    
    is_running = True
    while is_running:
        print('Choose a digit from 1 to 3!')
        key = util.key_pressed()
        player_choice = key
        if player_choice not in ('1', '2', '3'):
            print("Wrong input!")
            continue
        bot_choice = random.choice(game)
        time_left()
        bot_figlet = pyfiglet.figlet_format('Bot choice:', font='standard')
        print(Fore.BLUE + f'\n{bot_figlet}\n {bot_choice}')
        time.sleep(1)
        if player_choice == '1':
            if bot_choice == paper:
                draw()
                continue
            elif bot_choice == scissors:
                lost()
                return False
                is_running = False
            elif bot_choice == rock:
                win()
                return True
                is_running = False
        if player_choice == '2':
            if bot_choice == paper:
                win()
                return True
                is_running = False
            elif bot_choice == scissors:
                draw()
                continue
            elif bot_choice == rock:
                lost()
                return False
                is_running = False
        if player_choice == '3':
            if bot_choice == paper:
                lost()
                return False
                is_running = False
            elif bot_choice == scissors:
                win()
                return True
                is_running = False
            elif bot_choice == rock:
                draw()
                continue
        else: 
            print('Wrong value!')
            continue

            