import random
import time
import pyfiglet
from colorama import Fore, Style
import util
import threading


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
        key = util.key_pressed()
        player_choice = key
        print('Choose a digit from 1 to 3!')
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


riddles = [
    {'Take off my skin and I won’t cry, but you will, what am I?': 'Onion'},
    {'I am born of water but when I return to water, I die. What am I?': 'Ice'},
    {'I am always in front of you but never behind you. What am I?': 'Future'},
    {'What begins but has no end and is the ending of all that begins?': 'Death'},
    {'I am always hungry. I must be fed. Whatever I touch will soon turn red. What am I?': 'Fire'},
    {'I am a container with no sides and no lid, yet golden treasure lays inside. What am I?': 'Egg'},
    {'You can drop me from the tallest building and I’ll be fine, but if you drop me in fire I die. What am I?': 'Paper'},
    {'Sometimes I walk in front of you. Sometimes I walk behind you. It is only in the dark that I ever leave you. What am I?': 'Shadow'},
    {'I get smaller every time I take a bath. What am I?': 'Soap'},
    {'They come out at night without being called. They are lost in the day without being stolen. What are they?': 'Stars'},
]
def get_key(key):
    for k in key.keys():
        key = k
    return key

def get_value(key):
    for v in key.values():
        value = v
    return value

def quess_a_riddle():
    print(Fore.MAGENTA + """
        To open chest you have to quess the riddle of Pink Fairy. 
        She is really smart and tricksy.
        You have just 3 tries to guess a good answer. 
        Be careful and good luck!\n\n""" + Style.RESET_ALL)
    time.sleep(5)
    riddle = random.choice(riddles)
    key = get_key(riddle)
    value = get_value(riddle)
    tries = 3
    play_riddle = True
    while play_riddle:
        print(key)
        time.sleep(3)
        print(f'Tries: {tries}')
        player_choice = input('Your answer:\n')
        if player_choice == value:
            print("Great! You guessed it! Now open chest and check what is inside!")
            time.sleep(3)
            play_riddle = False
            return True
        elif player_choice != value:
            tries -= 1
            if tries > 0:
                print('That\'s not good answer. Try again!')
                time.sleep(3)
                continue
            elif tries == 0:
                print('You have no more tries! You lost!')
                time.sleep(3)
                play_riddle = False
                return False
            
