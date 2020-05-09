def is_boss_encounter(player, boss):

    boss_width = len(boss["icon"][0])
    boss_height = len(boss["icon"])
    boss_position_Y = boss["coordinates"]["Y"]
    boss_position_X = boss["coordinates"]["X"]    

    player_position_Y = player["coordinates"]["Y"]
    player_position_X = player["coordinates"]["X"]

    variation = 1

    if player_position_X in range(boss_position_X - variation, boss_position_X + boss_width + variation) and player_position_Y in range(boss_position_Y -variation, boss_position_Y + boss_height + variation):
        return True
    else:
        return False

def boss_combat_icon(player, boss):

    boss_width = len(boss["icon"][0])
    boss_height = len(boss["icon"])

    boss_position_Y = boss["coordinates"]["Y"]
    boss_position_X = boss["coordinates"]["X"]    

    player_position_Y = player["coordinates"]["Y"]
    player_position_X = player["coordinates"]["X"]

    icon_index_Y = player_position_Y - boss_position_Y
    icon_index_X = player_position_X - boss_position_X

    if icon_index_Y == -1:
        icon_index_Y += 1
    elif icon_index_Y == boss_height:
        icon_index_Y -= 1

    if icon_index_X == -1:
        icon_index_X += 1
    elif icon_index_X == boss_width:
        icon_index_X -= 1

    char_counter = 0
    updated_row = ""
    for char in boss["icon"][icon_index_Y]:
        if char_counter != icon_index_X:
            updated_row = updated_row + str(char)
        else:
            updated_row = updated_row + "X"
        char_counter += 1

    boss["icon"][icon_index_Y] = updated_row

def boss_original_icon(boss):
    row_index = 0
    for row in boss["icon"]:
        boss["icon"][row_index] = boss["original icon"][row_index]
        row_index += 1

def boss_dead_icon(boss):
    row_index = 0
    for row in boss["icon"]:
        boss["icon"][row_index] = boss["dead icon"][row_index]
        row_index += 1

def boss_combat(player, boss, MESSAGE):
    boss_name = boss["name"]
    player_attack = player["AD"] - boss["armour"]
    boss_attack = boss["AD"] - player["Armour"]

    player["Health"] -= boss_attack
    boss["health"] -= player_attack

    MESSAGE.append(f'{boss_name} hits you and you lose {boss_attack} health points.')
    MESSAGE.append(f'You hit the {boss_name} and he loses {player_attack} health points.')