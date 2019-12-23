import random

def print_header():
    print("--------------------------")

class Paper():

    def attack(self,roll):
        if roll == Rock():
            return True
        elif roll == Paper():
            return "Tie"
        elif roll == Scissors():
            return False

class Rock():

    def attack(self,roll):
        if roll == Scissors():
            return True
        elif roll == Rock():
            return "Tie"
        elif roll == Paper():
            return False

class Scissors():

    def attack(self,roll):
        if roll == Paper():
            return True
        elif roll == Scissors():
            return "Tie"
        elif roll == Rock():
            return False

rolls = [Paper(),Rock(),Scissors()]

def pc_rolls():
    return random.choice(rolls)

pc_roll = None


def ask_for_roll():
    user_input = input("What do you choose? ROCK, PAPER or SCISSORS? \n")
    if  user_input == "scissors":
        return Scissors()
    elif user_input == "rock":
        return Rock()
    elif user_input == "paper":
        return Paper()
         
def fight():
    pc_roll = pc_rolls()
    p_roll = ask_for_roll()
    #just to see if i was really supposed to win/lose/tie i can see what class was assigned to who
    print(str(p_roll))
    print(str(pc_roll))
    
    if p_roll.attack(pc_roll):
        return 1
    elif not p_roll.attack(pc_roll):
        return 2
    elif p_roll.attack(pc_roll) == "Tie":
        return 0

    
while True:
    print_header()
    
    for i in range(3):
        result = fight()
        if result == 1:
            print("You WON!")
        elif result == 2:
            print("You Lost!")
        elif result == 0:
            print("It is a TIE!")
    break    
    
