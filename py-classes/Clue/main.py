from clue import *

def main():
    game = Clue()
    number_of_players = int(input("Enter number of players: "))
    
    for i in range(number_of_players):
        game.create_player(input("Player Name: "))

    print(game.players)
    game.card_handout()

    while(True):
        for i in game.players:
            print(f"The player is {i.name} and their dice number is {game.roll_dice()}")
            for card in i.card_list:
                print(card.name)
        input()
if __name__ == "__main__":
    main()





