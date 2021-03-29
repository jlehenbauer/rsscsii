# Clue
## todo
1. weapons class
2. room class
3. character class
5. for each class make list of objects as a class variable
6. in each "\_\_init__" 
    1. choose who, what, and where.

## Assignments

##### _3/22/21_
Create `self.solution` list from random elements of item lists.

##### _3/23/21_
- Remove the items in `self.solution` from their respective lists
- Begin your `Player` class

##### _3/24/21_
Write the  `create_player` function and implement it inside `main.py`
 - create a player object (`Player(name)`) inside `create_player`
 - add player to `players` list
 - return player object
 - in `main.py`: for num_players: game.create_player(input("player name?"))

 ##### _3/25/21_
 Brainstorm and write down:
 1. What happens next in Clue
 2. What would it be useful for our Player objects to be able to do
 ### Kate:
 #### Next we will need to make and roll the dice 
 #### It would be useful to know proximity to a room and general location

##### _3/29/21_
1. Write `roll_dice` function in clue.py
2. Create loop in main.py for player turns
3. For each turn:
    1. Print who's turn it is
    2. Print their card list
    3. Print their dice roll