from clue import *

def main():
    game = Clue()
    number_of_players = int(input("Enter number of players: "))
    
    for i in range(number_of_players):
        game.create_player(input("Player Name: "))

    print(game.players)

    for i in game.players:
        print (i.name)
        print (i.card_list)
        print (roll_dice())
if __name__ == "__main__":
    main()





