import sys
import random
from enum import Enum

class ABC(Enum):

    STONE=1
    PAPER=2
    SCISSOR=3

print("")
playerchoice = input(
    " Enter...   \n1 for rock,\n2 for paper," \
    "\n3 for scissor:")

player=int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1,2 or 3")


computer_choice = random.choice("123")

computer= int(computer_choice)
print("")

string=""

print("YOU chose :"+str(ABC(player)).replace('ABC.','') +".")
print("computer chose :"+str(ABC(computer)).replace('ABC.','')+".")
print("")

if player == 1 and computer == 3:
    print("🥳YOU WIN!")
elif player == 2 and computer == 1:
    print("🥳YOU WIN!")
elif player == 3 and computer == 2:
    print("🥳YOU WIN!")
elif player == computer:
    print("😵TIE GAME!")
else:
    print("😒PYTHON WIN!")







