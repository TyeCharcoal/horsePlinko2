#7/24/23
#Tye

import time
import random

#Values
horse = "\U0001F40E"    # DO NOT EDIT HORSE VALUE
left = 40
right = 40
peg = "o"
air = " "
board = (peg + air) * left + horse + (air + peg) * right        #this is the formula to print the board
void = (air * 2) * left + horse + (air * 2) * right 

print(void)

"""
start = input("Would You Like To Play: Traditional [1], Random Encounter [2]")

#function to choose which side the horse falls to
def slide():
    x = random.randint(1,2)
    if x == 1:
        left + 1
    else:
        right + 1

print(board)


#Game
if start == 1:
"""

