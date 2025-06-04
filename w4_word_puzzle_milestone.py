"""Word Big Puzzle Milestone"""

secret_word = "mormon"  # The hidden secret word
attempts = 0  # Counter for the number of guesses

print("Welcome to the word guessing game!")

while True:
    guess = input("What is your guess? ").lower()
    attempts += 1
    
    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {attempts} guesses.")
        break
    else:
        print("Your guess was not correct.")
