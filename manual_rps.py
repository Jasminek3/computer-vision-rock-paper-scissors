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
    elif computer_choice == "Rock" & user_choice == "Paper":
        print("You Won")
    elif computer_choice == "Rock" & user_choice == "Scissors":
        print("You Lost")
    elif computer_choice == "Paper" & user_choice == "rock":
        print("You Lost")
    elif computer_choice == "Paper" & user_choice == "Scissors":
        print("You Won")
    elif computer_choice == "Scissors" & user_choice == "Rock":
        print("You Won")
    elif computer_choice == "Scissors" & user_choice == "Paper":
        print("You Lost")

get_winner("Rock", "Sissors")
# %%
