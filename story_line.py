import time
from colorama import Fore, Back, Style


story = [
        Fore.BLUE + "You are waking up in the world called Coloredia.",
        Fore.GREEN + "Everything is fabulous and colorful here.",
        Fore.MAGENTA + "No one is angry, there is no wars and fights.",
        Fore.BLUE + "Just happiness and joy!.",
        Fore.GREEN + "Unfortunatelly one bad, dark guy called Black Moaner.",
        Fore.MAGENTA + "Sent his Awfulers to destroy this world,",
        Fore.BLUE + "and make it dark, sad and dead...",
        Fore.GREEN + "Your main task is to kill all Awfulers and rescue Coloredia.",
        Fore.MAGENTA + "We all belive in you.",
        Fore.BLUE + "You are our last hope..." + Style.RESET_ALL
]

def display_story_line():
    story_line = story
    time.sleep(2)
    for line in story_line:
        print(line.rjust(100))
        print('')
        time.sleep(4)
    time.sleep(2)
    print(Fore.RED + "Press any key to back to menu" + Style.RESET_ALL)



