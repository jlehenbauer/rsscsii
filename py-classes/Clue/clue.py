class Clue:
    weaponsList = ["Candle Stick", "Knife", "Lead Pipe", "Revolver", "Rope", "Wrench"]
    murderersList = ["Colonel Mustard", "Mrs. White", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Miss Scarlet"]
    roomsList = ["Ballroom", "Billiard Room", "Conservatory", "Dining Room", 'Hall', "Kitchen", "Lounge", "Library", "Study"]

    
    def __init__(self):
        self.solution = []
        self.weapons = []

        for item in self.weaponsList:
            self.weapons.append(Weapon(item))
            self.solution.append(Weapon(item))

        self.murderer = []
        for item in self.murderersList:
            self.murderer.append(Murderer(item))
            self.solution.append(Murderer(item))

        self.rooms = []
        for item in self.roomsList:
            self.rooms.append(Room(item))
            self.solution.append(Room(item))

        
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





