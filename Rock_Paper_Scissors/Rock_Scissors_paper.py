import random

pos_actions = ["R", "P", "S"]

computer = random.choice(pos_actions)

player = False

while player == False:
    player = input("Please, Enter a choice (R, P, S): ")
    print(f"\nYou chose {player}, computer chose {computer}.\n")
    if player == computer:
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("You lose!")
        else:
            print("You win!")
    elif player == "P":
        if computer == "S":
            print("You lose!")
        else:
            print("You win!")
    elif player == "S":
        if computer == "R":
            print("You lose...")
        else:
            print("You win!")
    else:
        print("That's not a valid choice. Enter R, P or S!")
    
    player = False
    computer = random.choice(pos_actions)