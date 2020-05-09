import roguelike
import util
import story_line
import creators
import pyfiglet
from colorama import Fore, Back, Style

options = [
            "1) Play game",
            "2) Story line",
            "3) Creators",
            "4) Quit" 
]


def print_options(options):
    for element in options:
        print(Fore.GREEN + pyfiglet.figlet_format(element, font='big') + Style.RESET_ALL)
    

def run():
    roguelike.welcome()
    key = util.key_pressed()
    util.clear_screen()
    if key:
        is_playing_roguelike = True
        while is_playing_roguelike:
            print_options(options)
            key = util.key_pressed()
            util.clear_screen()
            if key == '1':
                roguelike.main()
                break
            elif key == '2':
                story_line.display_story_line()
                key = util.key_pressed()
                util.clear_screen()
                if key:
                    continue
            elif key == '3':
                creators.print_creators()
                key = util.key_pressed()
                util.clear_screen()
                if key: 
                    continue
            elif key == '4':
                break

run()



