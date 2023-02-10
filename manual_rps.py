#%%
import random

def get_computer_choice():
    cc = random.choice(["Rock", "Paper", "Scissors"])
    return cc

def get_user_choice():
    userInput = input("Enter your choice")
    return userInput

def get_winner(cc, userInput):
    if cc == userInput:
        print("Tie")
    elif userInput == "Rock":
        if cc == "Paper":
            print("You Lost")
        else:
            print("You Won!")
    elif userInput == "Paper":
        if cc == "rock":
                print("You Won")
        else:
                print("You Lost")
    elif userInput == "Scissors":
        if cc == "Rock":
            print("You Lost")
        else:
            print("You Won!")
    else:
        print("Error")

get_winner("Rock", "Sissors")
# %%
