"""Word Big Puzzle

Author: Nuno Ferreira

"""

import random

# List of possible secret words
word_list = ["faith", "temple", "prophet", "joseph", "restauration"]
secret_word = random.choice(word_list)  # Randomly select a secret word
attempts = 0  # Counter for the number of guesses

print("Welcome to the word guessing game!")
print("Your hint is:", "_ " * len(secret_word))

while True:
    guess = input("What is your guess? ").lower()
    attempts += 1
    
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue
    
    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {attempts} guesses.")
        break
    
    # Generate hint
    hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper() + " "  # Correct letter and position
        elif guess[i] in secret_word:
            hint += guess[i].lower() + " "  # Correct letter, wrong position
        else:
            hint += "_ "  # Letter not in word
    
    print("Your hint is:", hint.strip())
