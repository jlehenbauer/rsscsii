from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

"""
In all Karel projects, Karel only begins with the following
abilities:

move()
 - Karel moves one space in whichever direction they 
   are facing

turn_left()
 - Karel turns left once (90 degrees)

pick_beeper()
 - Karel picks up a beeper on Karel's current spot

put_beeper()
 - Karel places a beeper on Karel's current spot

See karel-reference.md for all Karel's capabilities.
"""


def main():
	pass
	turn_right()
	move()
	turn_left()
	move3()
	pick_beeper()
	turn180()
	move3()
	turn_right()
	move()

def turn_right():
	turn_left()
	turn_left()
	turn_left()

def move3():
	move()
	move()
	move()

def turn180():
	turn_left()
	turn_left()

	# There is no need to edit code below this line

if __name__ == "__main__":
    run_karel_program()
