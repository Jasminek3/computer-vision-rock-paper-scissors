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
        print("It is a tie!")
    elif cc == "Rock":
        if userInput == "Paper":
            print("You Won")
        else:
            print("You Lost")
    elif cc == "Paper":
        if userInput == "rock":
                print("You Lost")
        else:
                print("You Won")
    elif cc == "Scissors":
        if userInput == "Rock":
            print("You Won")
        else:
            print("You Lost")
    else:
        print("Error")

get_winner("Rock", "Sissors")
# %%
