'''
Adventure Game
Author: Takoda English
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.

'''


# welcome message and introduction
print("Welcome to the Adventure Game!")  
print('Your journey begins here...')

# ask for the player's name
player_name = input("What is your name, adventurer?")

# Concatenate strings to create a personlized message
print("Welcome, " + player_name + "! Your journey begins now. ")

# Use an f-string to display the same message in a more readable way
print(f"Welcome, {player_name}! Your journey begins now. ")

# Described the starting area
starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(starting_area)

# ask the player for their first decesion
decision = input("do you wish to take the path (yes or no): "). lower()

# Respond based on the player's deciision
if decision == "yes":
    print (f"Brave choice, {player_name}! You step on the path and venture foward")
elif decision == "no":
    print(f"{player_name}, you decide to wait. Perhaps courage will find you later. ")
else:
    print("Confused, you stand still, unsure of what to do")