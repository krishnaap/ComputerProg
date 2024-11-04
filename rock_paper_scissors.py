#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:44:12 2024

@author: krishna
"""
from random import randrange

def get_user_weapon():
    print("Select your weapon (1-3):\n =============================")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_choice = int(input("\n =================== \n Select your Weapon: "))
    return user_choice

def get_opponent_weapon():
    return randrange(1, 4)
    
def determine_winner(user_weapon, opponent_weapon):
    weapons = ["Rock", "Paper", "Scissors"]         # for displaying the weapon name instead of showing just a number
    user_weapon_name = weapons[user_weapon - 1]
    opponent_weapon_name = weapons[opponent_weapon - 1]
    if user_weapon == opponent_weapon:
        print(f"It's a tie!!. You both selected {user_weapon_name}")
    elif (user_weapon == 1 and opponent_weapon == 3) or \
         (user_weapon == 2 and opponent_weapon == 1) or \
         (user_weapon == 3 and opponent_weapon == 2):
        
        print(f"Congratulations! You win. {user_weapon_name} won against {opponent_weapon_name}")
    else:
        print(f"You lose. {opponent_weapon_name} beats {user_weapon_name}. Better luck next time!")

def main():
    continue_playing = 'y'
    while continue_playing.lower() == 'y':
        user_weapon = get_user_weapon()
        opponent_weapon = get_opponent_weapon()
        determine_winner(user_weapon, opponent_weapon)
        continue_playing = input("\n Would you like to continue playing? (y/n): ")
    print("Completed by, Krishnakumar AP")


if __name__ == "__main__":
    main()
