import random

def print_header():
    print("Welcome to Rock Paper Scissors!")

class Paper():
    def __init__(self):
        self.type = "paper"
    def attack(self,roll):
        if roll.type == "rock":
            return "win"
        elif roll.type == "paper":
            return "tie"
        elif roll.type == "scissors":
            return "lose"

class Rock():
    def __init__(self):
        self.type = "rock"
    def attack(self,roll):
        if roll.type == "scissors":
            return "win"
        elif roll.type == "rock":
            return "tie"
        elif roll.type == "paper":
            return "lose"

class Scissors():
    def __init__(self):
        self.type = "scissors"
    def attack(self,roll):
        if roll.type == "win":
            return True
        elif roll.type == "scissors":
            return "tie"
        elif roll.type == "rock":
            return "lose"

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
    #print(str(p_roll))
    #print(str(pc_roll))

    if p_roll.attack(pc_roll) == "win":
        return 1
    elif  p_roll.attack(pc_roll) == "lose":
        return 2
    elif p_roll.attack(pc_roll) == "tie":
        return 0

    
while True:
    print_header()
    p_score = 0
    pc_score = 0
    for i in range(3):
        print(f"Player.score: {p_score}")
        print(f"PC.....score: {pc_score}")
        result = fight()
        if result == 1:
            print("One point for you!")
            p_score +=1
        elif result == 2:
            print("One point to the enemy!")
            pc_score+=1
        elif result == 0:
            print("Noone gets anything")
    print(f"Player score: {p_score}")
    print(f"PC score: {pc_score}")
    if p_score > pc_score:
        print("Congratulations you won!")
    elif pc_score > p_score:
        print("You lost but i am sure that youll win next time")
    elif pc_score == p_score:
        print("It is a tie! Noone wins!")
    answer = input("do you want to play again? \n")
    if "y" in answer:
        continue
    else:
        print("Goodbye fellow gamer! See you next time.")
        break
        
    
    


