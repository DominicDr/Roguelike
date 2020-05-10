from colorama import Fore, Back, Style 
import time
import util

money = {
    'Silver Coin': {
        'name': 'Silver Coin', 
        'description': 'That\'s a silver coin. Use it to buy some stuff.',
        'type': 'money',
        'colour': 's',
        'sign': 'o',
        'amount': 5,
    },
}

armours = {
    'Leather Robe': {
        'name': 'Leather Robe',
        'description': 'Raddled, stained attire of peasant.',
        'type': 'armour',
        'durability': 5,
        'colour': 'b',
        'sign': 'A',
        'amount': 0,
    },
    'Silver Hauberk': {
        'name': 'Silver Hauberk', 
        'description': 'Pretty light and solid armour for assasin.',
        'type': 'armour',
        'durability': 10,
        'colour': 's',
        'sign': 'A',
        'amount': 0,
    },
    'Gold Plate': {
        'name': 'Gold Plate',
        'description': 'Shiny, incredibly durable armour for knight',
        'type': 'armour',
        'durability': 25,
        'colour': 'y', 
        'amount': 0,
    },
    'Platinum Armour': {
        'name': 'Platinum Armour', 
        'description': 'Divine, almost indestructible platinum plate armour! Only the \'Chosen one\' can put it on',
        'type': 'armour',
        'durability': 75,
        'colour': 'p',
        'sign': 'A',
        'amount': 0,
    }
    }

weapons = {
    'Wooden Mace': {
        'name': 'Wooden Mace',
        'description': 'Just a wood stick. Nothing more.',
        'type': 'weapon',
        'strength': 15,
        'colour': 'b',
        'sign': 'W',
        'amount': 0,
    },
    'Stone Hammer': {
        'name': 'Stone Hammer',
        'description': 'Do you know Thor, God of Thunder? Look\'s pretty similar, isn\'t it?',
        'type': 'weapon',
        'strenght': 35,
        'colour': 's',
        'sign': 'W',
        'amount': 0,
    },
    'Silver Dagger': {
        'name': 'Silver Dagger',
        'description': 'That\'s the most popular weapon of assassins of kings.',
        'type': 'weapon',
        'strenght': 50,
        'colour': 's',
        'sign': 'W',
        'amount': 0,  
    },
    'Iron Axe': {
        'name': 'Iron Axe', 
        'description': 'It\'s really sharp tool. Be careful with that and go kill some bastards!',
        'type': 'weapon',
        'strenght': 60,
        'colour': 'y',
        'sign': 'W',
        'amount': 0,
    },
    'Emerald Sword': {
        'name': 'Emerald Sword',
        'description': "If you thought that Excalibur was 'legendary and indestructible sword', you should try this one.", 
        'type': 'weapon',
        'strenght': 100,
        'colour': 'p', 
        'sign': 'W',
        'amount': 0,
    },
    }

foods = {
    'Apple': {
        'name': 'Apple', 
        'description': 'It\'s not a golden apple, but still tasty!',
        'type': 'food',
        'health': 10,
        'colour': 'b',
        'sign': 'F',
        'amount': 0,
    },
    'Bread': {
        'name': 'Bread',
        'description': 'Traditional, chrunchy bread. Will give you a lot of strenght!',
        'type': 'food',
        'health': 30, 
        'colour': 's',
        'sign': 'F',
        'amount': 0,
    },
    'Meat': {
        'name': 'Meat', 
        'description': 'Big portion of great red meat. Sound\'s good for everyone, except vegetarians.',
        'type': 'food',
        'health': 50,
        'colour': 'y',
        'sign': 'F',
        'amount': 0,
    }, 
    'Enchanted Glistening Onion': {
        'name': 'Enchanted Glistening Onion', 
        'description': 'That small, shiny vegetable will be your last hope one day. Trust me.',
        'type': 'food',
        'health': 100,
        'colour': 'p',
        'sign': 'F',
        'amount': 0,
    },
    }

artifacts = {
    'Phoenix\'s Heart': {
        'name': 'Phoenix\'s Heart',
        'description': 'Carefully! It\'s still very hot!',
        'type': 'artifact',
        'sign': '?',
        'amount': 0,
    },
    'Wild Lotus': {
        'name': 'Wild Lotus', 
        'description': 'You are lucky guy, if you found this flower. It\'s tremendously rare.', 
        'type': 'artifact',
        'sign': '?',
        'amount': 0,
    },
    'Moonlight': {
        'name': 'Moonlight', 
        'description': 'You got part of our holy moon. Use it well, my friend.',
        'type': 'artifact',
        'sign': '?',
        'amount': 0,
    },
    }

def add_stats(item, player):
    if 'strength' in item:
        player['AD'] += item['strength']
    elif 'durability' in item:
        player['Armour'] += item['durability']



def add_items_to_inventory(item, inventory, player):
    if type(item) is list:
        for element in item:
            if element in inventory:
                if element['amount'] == 0:
                    element['amount'] += 2
                else:
                    element['amount'] += 1
            else:
                inventory.append(element)
                add_stats(element, player)
    else:
        if item in inventory:
            if item['amount'] == 0:
                item['amount'] += 2
            else:
                item['amount'] += 1
        else:
            inventory.append(item)
            add_stats(item, player)


def print_item(item, item_key):
    item = str(item)
    item_to_print = '|' + (item_key) + ': ' + (item) + (((80 - (len(item) + len(item_key)))) * ' ') + '|'
    return item_to_print

def max_health(player):
    if player['Race'] == 'Warrior':
        max_health = 100
        return max_health
    if player['Race'] == 'Troll':
        max_health = 120
        return max_health
    if player['Race'] == 'Assassin':
        max_health = 80
        return max_health
    


def choose_item_to_eat(inventory, player):
    choosing_food = True
    while choosing_food:
        print("Press F to choose a food to eat or press X to back")
        key = util.key_pressed()
        if key == 'x':
            choosing_food = False
        elif key == 'f':
            chosen_food = input("Choose a food to eat\n")
            for element in inventory:
                if chosen_food == element['name']:
                    life = element['health']
                    player['Health'] += life
                    if player['Health'] > max_health(player):
                        player['Health'] = max_health(player)
                    element['amount'] -= 1
                    if element['amount'] < 0:
                        inventory.remove(element)
                    print(f'You just ate {chosen_food}')
                    time.sleep(3)
                    choosing_food = False
                else:
                    continue
        else:
            print('Wrong key!')
            continue
        
    
def display_inventory(inventory):
    inside_line = '|' + '=' * 82 + '|'
    outside_line = '-' * 82
    print(' ' + outside_line)
    for items in inventory:
        if items == inventory[-1]:
            print(print_item(items['name'], "Name"))
            print(print_item(items['description'], "Description"))
            if items['amount'] > 0:
                print(print_item(items['amount'], "Amount"))
                if 'strength' in items:
                    print(print_item(items['strength'], "Strength points"))
                elif 'durability' in items:
                    print(print_item(items['durability'], "Armor points"))
                # elif 'health' in items:
                #     print(print_item(items['health'], "Life points"))
            else: 
                if 'strength' in items:
                    print(print_item(items['strength'], "Strength points"))
                elif 'durability' in items:
                    print(print_item(items['durability'], "Armor points"))
                elif 'health' in items:
                    print(print_item(items['health'], "Life points"))
        elif items != inventory[-1]:
            print(print_item(items['name'], "Name"))
            print(print_item(items['description'], "Description"))
            if items['amount'] > 0:
                print(print_item(items['amount'], "Amount"))
                if 'strength' in items:
                    print(print_item(items['strength'], "Strength points"))
                elif 'durability' in items:
                    print(print_item(items['durability'], "Armor points"))
                elif 'health' in items:
                    print(print_item(items['health'], "Life points"))
            else: 
                if 'strength' in items:
                    print(print_item(items['strength'], "Strength points"))
                elif 'durability' in items:
                    print(print_item(items['durability'], "Armor points"))
                elif 'health' in items:
                    print(print_item(items['health'], "Life points"))
            print(inside_line)
    print(' ' + outside_line)




def print_player_life(player_life):
    upper_line = Fore.BLUE + Back.BLACK + '/' + player_life * '=' + '\\' 
    lower_line = Fore.BLUE + Back.BLACK + '\\' + player_life * '=' + '/' + Style.RESET_ALL
    life = range(player_life)
    print(Fore.BLUE + f'YOUR LIFE: {player_life} ❤'.center(95))
    if life == range(0, player_life):
        life_print = ''
        print(upper_line) 
        for i in life:
            if i == life[0]:
                life_print += '|❤'
            elif i == life[-1]:
                life_print += '❤|'
            else:
                life_print += '❤'
        print(Fore.RED + Back.BLACK + life_print + Style.RESET_ALL)
        print(lower_line)
    else:
        spaces = player_life - len(life)
        life_print = ''
        print(upper_line) 
        for i in life:
            if i == life[0]:
                life_print += '|❤'
            else:
                life_print += '❤'
        display_life = life_print + spaces * ' ' + '|'
        print(Fore.RED + Back.BLACK +  display_life + Style.RESET_ALL)
        print(lower_line)


chest1 = {
    "Secret chest": {
        'name': 'Secret Chest',
        'description': 'Huge, dusty chest. Would you like to check what is inside?',
        'coordinates': {'X': 10, 'Y': 15, },
        'items': [weapons['Wooden Mace'], armours['Leather Robe']],
        'icon': [Fore.YELLOW + Back.BLACK + '[' + Style.RESET_ALL, Fore.LIGHTWHITE_EX + Back.BLACK + '?' + Style.RESET_ALL, Fore.YELLOW + Back.BLACK + ']' + Style.RESET_ALL]

    } 
        
}


def put_full_chest_on_board(board, chest):
    chest_position_Y = chest["coordinates"]['Y']
    chest_position_X = chest["coordinates"]["X"]
    for element in chest['icon']:
        board[chest_position_Y][chest_position_X] = element
        chest_position_X += 1

def put_empty_chest_on_board(board, chest):
    chest_position_Y = chest["coordinates"]['Y']
    chest_position_X = chest["coordinates"]["X"]
    chest['icon'][1] = ' '
    for element in chest['icon']:
        board[chest_position_Y][chest_position_X] = element
        chest_position_X += 1

# def choose_item_to_eat(inventory, player):
#     choosing_food = True
#     while choosing_food:
#         print("Press F to choose a food to eat or press X to back")
#         key = util.key_pressed()
#         if key == 'x':
#             choosing_food = False
#         elif key == 'f':
#             chosen_food = input("Choose a food to eat\n")
#             for element in inventory:
#                 if chosen_food == element['name']:
#                     life = element['health']
#                     element['amount'] -= 1
#                     player['Health'] += life
#                     if element['amount'] < 0:
#                         inventory.remove(element)
#                     print(f'You just ate {chosen_food}')
#                     time.sleep(3)
#                     choosing_food = False
#                 else:
#                     continue
#         else:
#             print('Wrong key!')
#             continue