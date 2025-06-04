# Silly Story Maker program

print("Welcome to the Silly Story Maker!")

# Prompt user for inputs
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb1 = input("Enter a verb: ")
exclamation = input("Enter an exclamation: ").capitalize()
verb2 = input("Enter another verb: ")
verb3 = input("Enter one more verb: ")

# Story template
story = (
    f"The other day, I was really in trouble. It all started when I saw a very "
    f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all "
    f"I could think to do was to {verb2} over and over. Miraculously, "
    f"that caused it to stop, but not before it tried to {verb3} "
    f"right in front of my family."
)

# Display the final story
print("\nHere is your Silly Story:")
print(story)
