from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Karel moves across the room and records how many
    spaces they move. To do this, Karel places beepers
    at either end of the room, then rebounds between
    them, placing new beepers as Karel finds spaces
    without them. When Karel encounters a repeat beeper
    for the first time, the midpoint has been found!
    Clear all unnecessary beepers and return to the middle.
    """


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
