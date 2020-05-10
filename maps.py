map_blocks = [["-----",
    "|   |",
    "|   >",
    "-----"],
    ["-----",
    "> MM|",
    "|   >",
    "-----"],
    ["-----",
    ">   |",
    "|   >",
    "-----"],
    ["-----",
    "> ☻ |",
    "|   >",
    "-----"],
    ["-----",
    "> ☿ |",
    "|   |",
    "-----"]]

you_here = "✖"

def check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD):
    if current_map == WIZARD_BOARD:
        return 3
    elif current_map == SPIDER_BOARD + 1:
        return 1
    elif current_map == LAST_BOARD +1:
        return 4
    else:
        return 2

def print_map(player, MAP_COUNT, BOARD_COUNT, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD):
    blank_line = "     "
    lines_quantity = 4
    if MAP_COUNT > 1:
        lines_quantity += (MAP_COUNT - 1) * 2


    for line in range(lines_quantity):
        if lines_quantity == 4:
            print(map_blocks[0][line])
        elif lines_quantity == 6:

            if line in range(0,2):
                print(map_blocks[0][line] + (blank_line * MAP_COUNT))
            elif line in range(2,4):
                current_map = 2
                next_board = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(map_blocks[0][line] + map_blocks[next_board][line-current_map])
            elif line in range(4,6):
                current_map = 2
                next_board = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(blank_line * (current_map-1) + map_blocks[next_board][line-current_map])

        elif lines_quantity == 8:

            if line in range(0,2):
                print(map_blocks[0][line] + (blank_line * MAP_COUNT))
            elif line in range(2,4):
                current_map = 2
                next_board1 = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(map_blocks[0][line] + map_blocks[next_board1][line-2])
            elif line in range(4,6):
                current_map = 3
                next_board1 = check_board(current_map-1, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                next_board2 = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(blank_line + map_blocks[next_board1][line-2] + map_blocks[next_board2][line-4])
            elif line in range(6,8):
                current_map = 3
                next_board = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(blank_line * (current_map-1) + map_blocks[next_board][line-4])
        
        elif lines_quantity == 10:

            if line in range(0,2):
                print(map_blocks[0][line] + (blank_line * MAP_COUNT))
            elif line in range(2,4):
                current_map = 2
                next_board1 = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(map_blocks[0][line] + map_blocks[next_board1][line-2])
            elif line in range(4,6):
                current_map = 3
                next_board1 = check_board(current_map-1, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                next_board2 = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(blank_line + map_blocks[next_board1][line-2] + map_blocks[next_board2][line-4])
            elif line in range(6,8):
                current_map = 4
                next_board1 = check_board(current_map-1, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                next_board2 = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(blank_line * 2 + map_blocks[next_board1][line-4] + map_blocks[next_board2][line-6])
            elif line in range(8,10):
                current_map = 4
                next_board = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(blank_line * (current_map-1) + map_blocks[next_board][line-6])
    



            
        elif lines_quantity == 12:

            if line in range(0,2):
                print(map_blocks[0][line] + (blank_line * MAP_COUNT))
            elif line in range(2,4):
                current_map = 2
                next_board1 = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(map_blocks[0][line] + map_blocks[next_board1][line-2])
            elif line in range(4,6):
                current_map = 3
                next_board1 = check_board(current_map-1, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                next_board2 = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(blank_line + map_blocks[next_board1][line-2] + map_blocks[next_board2][line-4])
            elif line in range(6,8):
                current_map = 4
                next_board1 = check_board(current_map-1, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                next_board2 = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(blank_line * 2 + map_blocks[next_board1][line-4] + map_blocks[next_board2][line-6])
            elif line in range(8,10):
                current_map = 5
                next_board1 = check_board(current_map-1, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                next_board2 = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(blank_line * 3 + map_blocks[next_board1][line-6]+ map_blocks[next_board2][line-8])
            elif line in range(10,12):
                current_map = 5
                next_board = check_board(current_map, LAST_BOARD, SPIDER_BOARD, WIZARD_BOARD)
                print(blank_line * (current_map-1) + map_blocks[next_board][line-8])
            
        
 