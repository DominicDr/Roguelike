import Items
def create_wizard(Y, X):

    wizard = {
            'name': 'Wizard',
            'description': 'A friendly native inhabitant of this land',
            'health': 20,
            'AD': 1,
            'armour': 0,
            "coordinates": {"X": X, "Y": Y},
            "items": {"Wild Lotus": Items.artifacts["Wild Lotus"]},
            "icon":
    ["☻"]
    }

    return wizard