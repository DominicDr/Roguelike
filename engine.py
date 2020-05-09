import time
import copy
import random
import pyfiglet
from colorama import Fore, Back, Style

ALL_BORDER_COLORS = [1,4,6,9, '#']
ALL_FILL_COLORS = [2,5,7,8]
DOOR_COLOR = 3

def create_board(width, height, border_color=1, fill_color=2, border_width=2, doors_color=3):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    matrix = []

    for row in range(height):
        next_row = []
        for number in range(width):
            current_position = number + 1
            filling = width - (border_width * 2)
            if row < border_width or row >= height - border_width:
                next_row.append(border_color)
            elif current_position <= border_width or current_position > border_width + filling:
                next_row.append(border_color)
            else:
                next_row.append(fill_color)
        matrix.append(next_row)

    for index in range(border_width):
        door_placement_X = index - border_width
        door_placement_Y = border_width - border_width * 3
        matrix[door_placement_Y][door_placement_X] = doors_color

    return matrix



def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    player_position_X = player["coordinates"]["X"]
    player_position_Y = player["coordinates"]["Y"]
    player_icon = player["Player Icon"]

    board[player_position_Y][player_position_X] = player_icon


def put_chest_on_board(board, chest):
    chest_position_X = chest["coordinates"]["X"]
    chest_position_Y = chest["coordinates"]['Y']
    chest_icon = chest["Chest Icon"]

    board[chest_position_X][chest_position_Y] = chest_icon



def move_player(player, direction, board, original_board, MESSAGE):
    '''
    Modifies the game board by deleting the player from current position and changes the player's coordinates according to the direction chosen.
    Checks if the chosen place doesn't include a wall.

    Args:
    list: The game board
    list: The original game board copy without the player on it.
    str: Direction chosen by user
    int: Border color which defines the walls
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    player_position_X = player["coordinates"]["X"]
    player_position_Y = player["coordinates"]["Y"]

    board[player_position_Y][player_position_X] = original_board[player_position_Y][player_position_X]

    if direction == 'left':
        if board[player_position_Y][player_position_X - 1] in ALL_BORDER_COLORS:
            MESSAGE.append("You can't go through a wall")
        else:
            player["coordinates"]["X"] -= 1
    elif direction == 'right':
        if board[player_position_Y][player_position_X + 1] in ALL_BORDER_COLORS:
            MESSAGE.append("You can't go through a wall")
        else:
            player["coordinates"]["X"] += 1
    elif direction == 'up':
        if board[player_position_Y -1][player_position_X] in ALL_BORDER_COLORS:
            MESSAGE.append("You can't go through a wall")
        else:
            player["coordinates"]["Y"] -= 1
    elif direction == 'down':
        if board[player_position_Y + 1][player_position_X] in ALL_BORDER_COLORS:
            MESSAGE.append("You can't go through a wall")
        else:
            player["coordinates"]["Y"] += 1

def is_board_end(player, direction, BOARD_WIDTH, BOARD_HEIGHT, BOARD_COUNT, LAST_BOARD):
    
    if BOARD_COUNT == LAST_BOARD + 1:
        return False
    elif direction == 'down'and player["coordinates"]["Y"] + 1 == BOARD_HEIGHT:
        return True
    elif direction == 'right' and player["coordinates"]["X"] + 1 == BOARD_WIDTH:
        return True

def is_previous_board(player, direction):
    if direction == 'up'and player["coordinates"]["Y"] == 0:
        return True
    elif direction == 'left' and player["coordinates"]["X"] == 0:
        return True
    else:
        return False

def get_next_board(board, original_board, player, gnome, BOARD_WIDTH, BOARD_HEIGHT, border_color,fill_color, doors_color=3, border_width=2):

        next_board = create_board(BOARD_WIDTH, BOARD_HEIGHT, border_color, fill_color, border_width)

        for index in range(border_width):
            door_placement_X = index
            door_placement_Y = border_width * 2
            next_board[door_placement_Y][door_placement_X] = doors_color

            player["coordinates"]["X"] = door_placement_X
            player["coordinates"]["Y"] = door_placement_Y

            gnome["coordinates"]["X"] = door_placement_X + 1
            gnome["coordinates"]["Y"] = door_placement_Y

        board[:] = next_board
        original_board[:] = copy.deepcopy(next_board)

def get_last_board(board, original_board, player, gnome, BOARD_WIDTH, BOARD_HEIGHT, border_color,fill_color, doors_color=3, border_width=2):

    matrix = []

    for row in range(BOARD_HEIGHT):
        next_row = []
        for number in range(BOARD_WIDTH):
            current_position = number + 1
            filling = BOARD_WIDTH - (border_width * 2)
            if row < border_width or row >= BOARD_HEIGHT - border_width:
                next_row.append(border_color)
            elif current_position <= border_width or current_position > border_width + filling:
                next_row.append(border_color)
            else:
                next_row.append(fill_color)
        matrix.append(next_row)

    for index in range(border_width):
        door_placement_X = index
        door_placement_Y = border_width * 2
        matrix[door_placement_Y][door_placement_X] = doors_color

        player["coordinates"]["X"] = door_placement_X
        player["coordinates"]["Y"] = door_placement_Y

        gnome["coordinates"]["X"] = door_placement_X - 1
        gnome["coordinates"]["Y"] = door_placement_Y

    board[:] = matrix
    original_board[:] = copy.deepcopy(matrix)


def put_boss_on_board(board, boss):

    boss_position_Y = boss["coordinates"]["Y"]
    boss_icon = boss["icon"]

    for row in boss_icon:
        boss_position_X = boss["coordinates"]["X"]
        for char in row:
            board[boss_position_Y][boss_position_X] = char
            boss_position_X += 1
        boss_position_Y += 1

def remove_boss(boss, board, original_board):
    boss_icon = boss["icon"]

    boss_position_Y = boss["coordinates"]["Y"]
    for row in boss_icon:
        boss_position_X = boss["coordinates"]["X"]
        for char in row:
            board[boss_position_Y][boss_position_X] = original_board[boss_position_Y][boss_position_X]
            boss_position_X += 1
        boss_position_Y += 1


def move_boss(boss, boss_direction, board, original_board):
    
    remove_boss(boss, board, original_board)

    boss_position_Y = boss["coordinates"]["Y"]
    boss_position_X = boss["coordinates"]["X"]
    boss_width = len(boss["icon"][0])
    boss_height = len(boss["icon"])


    if boss_direction == 'left':
        if board[boss_position_Y][boss_position_X - 1] not in ALL_BORDER_COLORS and board[boss_position_Y][boss_position_X - 1] != DOOR_COLOR:
            boss["coordinates"]["X"] -= 1
    elif boss_direction == 'right':
        if board[boss_position_Y][boss_position_X + boss_width] not in ALL_BORDER_COLORS and board[boss_position_Y][boss_position_X + boss_width] != DOOR_COLOR:
            boss["coordinates"]["X"] += 1
    elif boss_direction == 'up':
        if board[boss_position_Y -1][boss_position_X] not in ALL_BORDER_COLORS:
            boss["coordinates"]["Y"] -= 1
    elif boss_direction == 'down':
        if board[boss_position_Y + boss_height][boss_position_X] not in ALL_BORDER_COLORS:
            boss["coordinates"]["Y"] += 1
        
def nearest_direction_to_player(boss, player):
    all_directions = ["up", "left", "right", "down"]

    boss_position_Y = boss["coordinates"]["Y"]
    boss_position_X = boss["coordinates"]["X"]

    boss_width = len(boss["icon"][0])
    boss_height = len(boss["icon"])

    player_position_X = player["coordinates"]["X"]
    player_position_Y = player["coordinates"]["Y"]

    subtraction_X = boss_position_X - player_position_X
    subtraction_Y = boss_position_Y - player_position_Y

    if abs(subtraction_X) > abs(subtraction_Y):
        if subtraction_X > 0:
            direction = all_directions[1]
        elif subtraction_X < boss_width:
            direction = all_directions[2]
        else:
            direction = random.choice(all_directions)

    elif abs(subtraction_Y) > abs(subtraction_X):
        if subtraction_Y > 0:
            direction = all_directions[0]
        elif subtraction_Y < boss_height:
            direction = all_directions[3]
        else:
            direction = random.choice(all_directions)
    else:
        direction = random.choice(all_directions)

    return direction

def get_npc_direction(npc, board, BOARD_HEIGHT, BOARD_WIDTH, border_width=2):
    all_directions = ["up", "left", "right", "down"]

    npc_position_Y = npc["coordinates"]["Y"]
    npc_position_X = npc["coordinates"]["X"]

    if npc_position_Y == BOARD_HEIGHT - border_width*2 and npc_position_X in range(border_width*2 -1, BOARD_WIDTH - (border_width*2)):
        direction = all_directions[2]
    elif npc_position_Y == border_width*2 - 1 and npc_position_X in range(border_width*2, BOARD_WIDTH - border_width*2 + 1):
        direction = all_directions[1]
    elif npc_position_X == BOARD_WIDTH - (border_width*2) and npc_position_Y in range(border_width*2, BOARD_HEIGHT - border_width*2 + 1):
        direction = all_directions[0]
    else:
        direction = all_directions[3]

    return direction

def welcome_screen():
    welcome = pyfiglet.figlet_format('Welcome in game...', font='ogre')
    print(Fore.RED + welcome.center(20) + Style.RESET_ALL)
    time.sleep(3)
    display_welcome_screen1 = pyfiglet.figlet_format("Rainbow", font='banner3')
    display_welcome_screen2 = pyfiglet.figlet_format("Tales", font='banner3')
    print(Fore.MAGENTA + display_welcome_screen1 + Style.RESET_ALL)
    print(Fore.CYAN + display_welcome_screen2 + Style.RESET_ALL)