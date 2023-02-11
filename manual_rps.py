#%%
import random

def get_computer_choice():
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    return print(computer_choice)

def get_user_choice():
    user_choice = input("Enter your choice")
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == "Rock" and user_choice == "Paper":
        return "You Won!"
    elif computer_choice == "Rock" and user_choice == "Scissors":
        return "You Lost"
    elif computer_choice == "Paper" and user_choice == "Scissors":
        return "You Won!"
    elif computer_choice == "Paper" and user_choice == "Rock":
        return "You Lost"
    elif computer_choice == "Scissors" and user_choice == "Rock":
        return "You Won!"
    elif computer_choice == "Scissors" and user_choice == "Paper":
        return "You Lost"
    else:
        print("It is a tie!")
        return "It is a tie!"

get_winner()
# %%