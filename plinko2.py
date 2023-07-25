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
board1 = (air + peg) * left + horse + (peg + air) * right        #this is the formula to print the boards larger variant
board2 = air + (air + peg) * (left - 1) + horse + (peg + air) * right
void = (air * 2) * left + horse + (air * 2) * right 


#function to choose which side the horse falls to
def slide():
    time.sleep(.5)
    x = random.randint(1,2)
    if x == 1:
        left += 1
        right -= 1
        print(board1)
    else:
        left -= 1
        right += 1
        print(board1)

#Game
print(board1)
for n in range(100):
    slide()



