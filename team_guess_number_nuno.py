"""
Author: Team Collaboration

Purpose: Guess My Number game designed for group discussion and problem-solving.
"""

import random

# Core Requirements Version
print("Welcome to the Group Guess My Number Game - Core Requirements!")
magic_number = random.randint(1, 100)
guess = -1

while guess != magic_number:
    guess = int(input("Enter your team's guess: "))
    
    if guess < magic_number:
        print("Higher! Try again.")
    elif guess > magic_number:
        print("Lower! Try again.")
    else:
        print("Congratulations, you guessed it!")

# Stretch Challenge Version
print("\nWelcome to the Group Guess My Number Game - Stretch Challenge!")
keep_playing = "yes"

while keep_playing.lower() == "yes":
    magic_number = random.randint(1, 100)
    guess_count = 0
    guess = -1
    
    print("The computer has chosen a random number between 1 and 100.")

    while guess != magic_number:
        guess = int(input("Enter your team's guess: "))
        guess_count += 1
        
        if guess < magic_number:
            print("Higher! Try again.")
        elif guess > magic_number:
            print("Lower! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {guess_count} attempts!")
    
    keep_playing = input("Would you like to play again? (yes/no): ")
