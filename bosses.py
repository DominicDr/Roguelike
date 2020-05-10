from colorama import Fore, Back, Style

def create_boss():
    boss = {
        "Big Bad Demon": {
            'name': 'Demon',
            'description': 'An abomination from outer space',
            'health': 666,
            'AD': 90,
            'armour': 6,
            "coordinates": {"X": 40, "Y": 20},
            "icon": 
    [" /\  /\ ",
    "( ,   ,)",
    "   ^^^  ",
    "    T   ",
    "  _/ \_ " ],
            "original icon": 
    [" /\  /\ ",
    "( ,   ,)",
    "   ^^^  ",
    "    T   ",
    "  _/ \_ "],
            "dead icon": 
    ["  ||   ",
    "   ||   ",
    "===||===",
    "   ||   ",
    "(R.I.P.)"]
        }}

    return boss["Big Bad Demon"]

def create_spider(Y, X):

    spider = {
            'name': 'Spider',
            'description': 'Just a very fast deadly, posionous spider. Very common',
            'health': 20,
            'AD': 1,
            'armour': 0,
            "coordinates": {"X": X, "Y": Y},
            "icon": ["/\;;/\\" ],
            "original icon": ["/\;;/\\"],
            "dead icon": ["<<::>>"],
        }

    return spider