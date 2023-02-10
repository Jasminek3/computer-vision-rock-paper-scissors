#%%
import random

def get_computer_choice():
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    return computer_choice

def get_user_choice():
    user_choice = input("Enter your choice")
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It is a tie!")
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            print("You Won!")
        else:
            print("You Lost")
    elif computer_choice == "Paper":
        if user_choice == "Rock":
                print("You Lost")
        else:
                print("You Won!")
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            print("You Won!")
        else:
            print("You Lost")
    elif computer_choice == "Scissors":
        if user_choice == "Paper":
            print("You Lost!")
        else:
            print("You Won!")

get_winner()
# %%
