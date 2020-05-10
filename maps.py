map_blocks = [["-----",
    "|   |",
    "|   >",
    "-----"],
    ["-----",
    "> M M|",
    "|   >",
    "-----"],
    ["-----",
    ">    |",
    "|   >",
    "-----"],
    ["-----",
    "| ☻ |",
    "|   >",
    "-----"],
    ["-----",
    "> ☿ |",
    "|   |",
    "-----"]]

you_here = "✖"

def check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD):
    if current_map == SPIDER_BOARD:
        return 1
    elif current_map == WIZARD_BOARD:
        return 3
    elif current_map == LAST_BOARD:
        return 4
    else:
        return 2

def print_map(player, MAP_COUNT, BOARD_COUNT, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD):
    blank_line = "     "
    lines_quantity = 4
    if MAP_COUNT > 1:
        lines_quantity += (MAP_COUNT - 1) * 2

    for line in range(lines_quantity):
        if line in range(0,2):
            print(map_blocks[0][line] + (blank_line * MAP_COUNT))
        elif line in range(2,4):
            current_map = 2
            next_board = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
            print(map_blocks[0][line] + map_blocks[next_board][line-2] + blank_line * (MAP_COUNT -1))
        
 