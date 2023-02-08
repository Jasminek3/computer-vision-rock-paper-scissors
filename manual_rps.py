#%%
import random

def get_computer_choice():
    cc = random.choice(["Rock", "Paper", "Scissors"])
    return cc

def get_user_choice():
    userInput = input("Enter your choice")
    return userInput

get_computer_choice()
get_user_choice()
# %%
