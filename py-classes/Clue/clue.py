import random

class Clue:
    weaponsList = ["Candle Stick", "Knife", "Lead Pipe", "Revolver", "Rope", "Wrench"]
    murderersList = ["Colonel Mustard", "Mrs. White", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Miss Scarlet"]
    roomsList = ["Ballroom", "Billiard Room", "Conservatory", "Dining Room", 'Hall', "Kitchen", "Lounge", "Library", "Study"]
    players = []
    
    def __init__(self):
        self.weapons = []
        self.murderer = []
        self.rooms = []
        self.solution = []

        for item in self.weaponsList:
            self.weapons.append(Weapon(item))

        for item in self.murderersList:
            self.murderer.append(Murderer(item))

        for item in self.roomsList:
            self.rooms.append(Room(item))

        self.solution = [random.choice(self.weapons), random.choice(self.murderer), random.choice(self.rooms)]
        
        self.weapons.remove(self.solution[0])
        self.murderer.remove(self.solution[1])    
        self.rooms.remove(self.solution[2])

    def create_player(self, name):
        player = Player(name)
        self.players.append(player)
        return player

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

class Player:
    name = None
    def __init__(self, name):
        self.name = name





