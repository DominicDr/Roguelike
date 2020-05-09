from colorama import Fore, Back, Style
import pyfiglet
import util
import engine
import ui
import data_management
import copy
import random
import os
import Items
import bosses
import champs
import combat
import mini_games
import time
import npc

PLAYER_ICON = Fore.GREEN + Back.LIGHTBLUE_EX + '▣' + Style.RESET_ALL
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

LAST_BOARD = 4
BOARD_COUNT = 1
SPIDER_BOARD = random.randint(BOARD_COUNT + 1, LAST_BOARD-1)
WIZARD_BOARD = BOARD_COUNT + 1
GATES_CLOSED = True

MESSAGE = []

PLAYER_INVENTORY = [Items.money['Silver Coin'], Items.foods['Apple'], Items.foods['Bread']]

FIRST_CHEST = Items.chest1['Secret chest']

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
        "Player Icon": PLAYER_ICON,
        "coordinates": {"X": PLAYER_START_X, "Y": PLAYER_START_Y},
        "Name": '',
        "Health": 0,
        "AD": 0,
        "Armour": 0,
        "Race": '',
        "Inventory": PLAYER_INVENTORY,
            }

    return player


def get_new_board(board, original_board, player):
    if BOARD_COUNT == LAST_BOARD:
        get_last_board(board, original_board, player)
        MESSAGE.append("This is the last chamber.")
    else:
        border_color = random.choice(engine.ALL_BORDER_COLORS[:-1])
        fill_color = random.choice(engine.ALL_FILL_COLORS)
        engine.get_next_board(board, original_board, player, BOARD_WIDTH, BOARD_HEIGHT, border_color, fill_color, doors_color=3, border_width=2)

def get_last_board(board, original_board, player):
    border_color = random.choice(engine.ALL_BORDER_COLORS[:-1])
    fill_color = random.choice(engine.ALL_FILL_COLORS)
    width = BOARD_WIDTH * 3
    height = BOARD_HEIGHT * 2
    engine.get_last_board(board, original_board, player, width, height, border_color, fill_color, doors_color=3, border_width=4)

def save_board(original_board):
    file_to_export = f'boards/board{BOARD_COUNT}.txt'
    data_management.write_board_to_file(file_to_export, original_board)

def get_previous_board(board, BOARD_COUNT, original_board, player, direction, border_width=2):


    if direction =='right' or direction == 'down':
        BOARD_COUNT += 1
    file_to_import = f'boards/board{BOARD_COUNT}.txt'
    board[:] = data_management.get_board_from_file(file_to_import)
    original_board[:] = copy.deepcopy(board)

    if BOARD_COUNT - 1 == LAST_BOARD:
        border_width = 4

    if direction == 'left' or direction == 'up':
        player["coordinates"]["X"] = BOARD_WIDTH - border_width
        player["coordinates"]["Y"] = BOARD_HEIGHT - border_width * 2

    elif direction =='right' or direction == 'down':
        player["coordinates"]["X"] = border_width - 1
        player["coordinates"]["Y"] = border_width * 2
    
def boss_on_board(player, boss, board, original_board):
    if BOARD_COUNT == LAST_BOARD + 1 and boss["health"] > 0:
        boss_direction = random.choice(["up", "left", "right", "down"])
        engine.move_boss(boss, boss_direction, board, original_board)
            
        if combat.is_boss_encounter(player, boss):
            combat.boss_combat_icon(player,boss)
            combat.boss_combat(player, boss, MESSAGE)

        engine.put_boss_on_board(board, boss)
        combat.boss_original_icon(boss)

    elif BOARD_COUNT == LAST_BOARD + 1 and boss["health"] <= 0:
        combat.boss_dead_icon(boss)
        engine.put_boss_on_board(board, boss)
        engine.put_player_on_board(board, player)

def spiders_on_board(player, spider, board, original_board):
    if BOARD_COUNT == SPIDER_BOARD + 1 and spider["health"] > 0:
        spider_direction = engine.nearest_direction_to_player(spider, player)
        engine.move_boss(spider, spider_direction, board, original_board)
            
        if combat.is_boss_encounter(player, spider):
            combat.boss_combat_icon(player,spider)
            combat.boss_combat(player, spider, MESSAGE)

        engine.put_boss_on_board(board, spider)
        combat.boss_original_icon(spider)

    elif BOARD_COUNT == SPIDER_BOARD + 1 and spider["health"] <= 0:
        combat.boss_dead_icon(spider)
        engine.put_boss_on_board(board, spider)
        engine.put_player_on_board(board, player)

def wizard_on_board(player, wizard, board, original_board, spider_one, spider_two):
    if BOARD_COUNT == WIZARD_BOARD and wizard["health"] > 0:
        wizard_direction = engine.get_npc_direction(wizard, board, BOARD_HEIGHT, BOARD_WIDTH)
        engine.move_boss(wizard, wizard_direction, board, original_board)

        if combat.is_boss_encounter(player, wizard) and spider_one["health"] > 0 or combat.is_boss_encounter(player, wizard) and spider_two["health"] > 0:
            MESSAGE.append("Wizard says: Hello adventurer!")
            MESSAGE.append("Wizard says: Please help us defeat the evil lord!")
            MESSAGE.append("Wizard says: I can give you the key to open his chamber, but please defeat the nearby spiders first.")
        
        elif combat.is_boss_encounter(player, wizard,):
            MESSAGE.append("Wizard says: Thank you for defeating those spiders!")
            if "Wild Lotus" in wizard["items"]:
                item = [Items.artifacts["Wild Lotus"]]
                Items.add_items_to_inventory(item, PLAYER_INVENTORY)
                MESSAGE.append("Take this 'Wild Lotus'. It will open the gates to the last chamber.")
                del wizard["items"]["Wild Lotus"]

        engine.put_boss_on_board(board, wizard)


def get_gates(player, wizard, board, original_board, border_width=2):
    global GATES_CLOSED
    if BOARD_COUNT == LAST_BOARD:
        gate_placement_X = BOARD_WIDTH - border_width
        gate_placement_Y = BOARD_HEIGHT - border_width * 2
        board[gate_placement_Y][gate_placement_X] = "#"
    
        if player["coordinates"]["Y"] == gate_placement_Y and player["coordinates"]["X"] + 1 == gate_placement_X and "Wild Lotus" in wizard["items"]:
            MESSAGE.append("You see a closed gate with a lotus painted on it, you can't force it.")
        elif player["coordinates"]["Y"] == gate_placement_Y and player["coordinates"]["X"] + 1 == gate_placement_X and board[gate_placement_Y][gate_placement_X] == "#":
            MESSAGE.append("You have opened the gate by placing the 'Wild Lotos' on it's painting")
            board[gate_placement_Y][gate_placement_X] = original_board[gate_placement_Y][gate_placement_X]
            GATES_CLOSED = False


def play_game(player, chest, board):
    if player['coordinates']['X'] - 1 == chest['coordinates']['X'] and player['coordinates']['Y'] == chest['coordinates']['Y']:
        if 'items' in FIRST_CHEST: 
            util.clear_screen()
            game = mini_games.play_game()
            mini_game_running = True
            while mini_game_running:
                if game is True: 
                    Items.add_items_to_inventory(FIRST_CHEST['items'], PLAYER_INVENTORY)
                    Items.put_empty_chest_on_board(board, FIRST_CHEST)
                    FIRST_CHEST.pop('items')
                    util.clear_screen()
                    mini_game_running = False
                elif game is False:
                    player['coordinates']['X'] = 8
                    player['coordinates']['Y'] = 8
                    util.clear_screen()
                    mini_game_running = False
        else:
            MESSAGE.append('Chest is empty')  

def welcome():
    engine.welcome_screen()
    print('Press any key to continue')  


def main():
    global BOARD_COUNT
    player = create_player() 
    util.clear_screen()
    # if key:
    name = input(Fore.BLUE + "What is your name, warrior?\n" + Style.RESET_ALL)
    player['Name'] = name
    util.clear_screen()
    champs.choose_a_character()
    champ_running = True
    while champ_running:
        key = util.key_pressed()
        if key == '1':
            player['Health'] += 100
            player['AD'] += 15
            player['Race'] += 'Warrior' 
            champ_running = False
        elif key == '2':
            player['Health'] += 120
            player['AD'] += 5
            player['Race'] += 'Troll'
            champ_running = False
        elif key == '3':
            player['Health'] += 80
            player['AD'] += 25
            player['Race'] += 'Assassin'
            champ_running = False
        else:
            print("Wrong key!")
            continue
    chest = Items.chest1['Secret chest']
    boss = bosses.create_boss()
    spider_one = bosses.create_spider(5, 21)
    spider_two = bosses.create_spider(15, 21)
    wizard = npc.create_wizard(5,17)
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    original_board = copy.deepcopy(board)
    save_board(copy.deepcopy(original_board))
    util.clear_screen()
    is_running = True
    while is_running:
        player_life = player['Health']
        Items.print_player_life(player_life)
        engine.put_player_on_board(board, player)
        if GATES_CLOSED:
            get_gates(player, wizard, board, original_board)
        boss_on_board(player, boss, board, original_board)
        spiders_on_board(player, spider_one, board, original_board)
        spiders_on_board(player, spider_two, board, original_board)
        wizard_on_board(player, wizard, board, original_board,spider_one, spider_two)

        if BOARD_COUNT == 1:
            Items.put_full_chest_on_board(board, FIRST_CHEST)
            play_game(player, chest, board)
        ui.display_board(board)
        if player_life < 0:
            util.clear_screen()
            lost = Fore.RED + pyfiglet.figlet_format('YOU DIED'.center(100), font='epic') + Style.RESET_ALL
            print(lost)
            time.sleep(3)
            print('Press any key to back to menu')
            key = util.key_pressed()
            if key:
                util.clear_screen()
                is_running = False
        for messages in MESSAGE:
            print(messages)
        MESSAGE[:] = []
        key = util.key_pressed()
        if key == 'q':
            quit_game = True
            while quit_game:
                util.clear_screen()
                print("Do you really want to quit? Y/N")
                key = util.key_pressed()
                if key == 'y':
                    quit_game = False
                    is_running = False
                elif key == 'n':
                    quit_game = False
                else:
                    print('Unknown command!')
                    time.sleep(2)
                    continue
        elif key == 'a':
            if engine.is_previous_board(player, 'left'):
                BOARD_COUNT -= 1
                get_previous_board(board,BOARD_COUNT, original_board, player, 'left', border_width=2)
            engine.move_player(player, 'left', board, original_board, MESSAGE)

        elif key == 'w':
            if engine.is_previous_board(player, 'up'):
                BOARD_COUNT -= 1
                get_previous_board(board, BOARD_COUNT, original_board, player, 'up', border_width=2)
            engine.move_player(player, 'up', board, original_board, MESSAGE)

        elif key == 's':
            if engine.is_board_end(player, 'down', BOARD_WIDTH, BOARD_HEIGHT, BOARD_COUNT, LAST_BOARD):
                try:
                    get_previous_board(board, BOARD_COUNT, original_board, player, 'down', border_width=2)
                    BOARD_COUNT += 1
                except FileNotFoundError:
                    get_new_board(board, original_board, player)
                    BOARD_COUNT += 1
                    save_board(copy.deepcopy(original_board))
            engine.move_player(player, 'down', board, original_board, MESSAGE)

        elif key == 'd':
            if engine.is_board_end(player, 'right', BOARD_WIDTH, BOARD_HEIGHT, BOARD_COUNT, LAST_BOARD):
                try:
                    get_previous_board(board, BOARD_COUNT, original_board, player, 'right', border_width=2)
                    BOARD_COUNT += 1
                except FileNotFoundError:
                    get_new_board(board, original_board, player)
                    BOARD_COUNT += 1
                    save_board(copy.deepcopy(original_board))
            engine.move_player(player, 'right', board, original_board, MESSAGE)
        
        elif key == 'i':
            Items.display_inventory(PLAYER_INVENTORY)
            print('Press any key to continue')
            key = util.key_pressed()
            
        else:
            MESSAGE.append("Incorrect input!")
        util.clear_screen()


    filelist = [ f for f in os.listdir("boards/") if f.endswith(".txt") ]
    for f in filelist:
        os.remove(os.path.join("boards/", f))

