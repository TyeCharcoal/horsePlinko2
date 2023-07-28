#7/28/23
#Tye

import time
import random

#Values
horse = "\U0001F40E"    # DO NOT EDIT HORSE VALUE
left = 40
right = 40
peg = "o"
air = " "

#functions for board printing
def print_board1():
    board1 = (air + peg) * left + horse + (peg + air) * right
    print(board1)

def print_board2():
    board2 = air + (air + peg) * (left - 1) + horse + (peg + air) * right
    print(board2)

def print_void():
    void = (air * 2) * left + horse + (air * 2) * right 
    print(void)

#function to choose which side the horse falls to
def slide():
    time.sleep(.5)
    x = random.randint(1,2)
    if x == 1:
        left + 1
        right - 1
        print_board1()
    else:
        left - 1
        right + 1
        print_board1()

#Game
print_board1()
for n in range(100):
    slide()
