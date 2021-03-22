class Clue:
    myList = None
    weaponsList = ["Candle Stick", "Knife", "Lead Pipe", "Revolver", "Rope", "Wrench"]
    murderersList = ["Colonel Mustard", "Mrs. White", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Miss Scarlet"]
    roomsList = ["Ballroom", "Billiard Room", "Conservatory", "Dining Room", 'Hall', "Kitchen", "Lounge", "Library", "Study"]

    
    def __init__(self):
        self.listLen = len(myList)
        self.weapons = []
        for item in weaponsList:
            self.weapons.append(Weapon(item))

        self.murderer = []
        for item in murderersList:
            self.murderer.append(Murderer(item))

        self.rooms = []
        for item in roomsList:
            self.rooms.append(Room(item))

class Weapon:
    name = None
    def __init__(self, name):
        self.name = name

class Murderer:
    name = None
    def __init__(self, name):
        self.name = name


class Room:
    name = None
    def __init__(self, name):
        self.name = name





