import random

# Generate a random number between 1 and 100
magic_number = random.randint(1, 100)

guess = None  # Initialize the guess variable

print("Welcome to the Guess My Number game!")

while guess != magic_number:
    guess = int(input("What is your guess? "))
    
    if guess < magic_number:
        print("Higher")
    elif guess > magic_number:
        print("Lower")
    else:
        print("Congratulations! You guessed it!")