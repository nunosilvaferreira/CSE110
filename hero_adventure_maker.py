# Hero Adventure Maker

print("Welcome to the Hero Adventure Maker!")
print("Create your own hero and embark on an epic quest!")

# Prompt user for hero details
hero_name = input("Enter your hero's name: ")
skill = input("What is your hero's special skill (e.g., invisibility, strength): ")
weapon = input("What is your hero's weapon of choice (e.g., sword, bow): ")
mission = input("What is your hero's mission (e.g., rescue a friend, find a treasure): ")
origin = input("Where is your hero from (e.g., a small village, a bustling city): ")
ally = input("Who is your hero's closest ally: ")
enemy = input("Who is your hero's greatest enemy: ")

# Generate the story
story = (
    f"In the quiet {origin}, a hero named {hero_name} was born. Known for their incredible ability to {skill}, "
    f"{hero_name} quickly became a legend among the people. Armed with their trusty {weapon}, they set out on a mission to {mission}. "
    f"Accompanied by their loyal friend {ally}, they faced countless challenges along the way.\n"
    f"But the greatest challenge was yet to come: a face-off with the dreaded {enemy}. "
    f"With courage, wit, and their {weapon}, {hero_name} overcame all odds and proved that even the smallest origins can produce the greatest heroes."
)

# Display the final story
print("\nHere is your Hero's Adventure:")
print(story)

print("\nThank you for crafting a heroic tale! May your hero inspire many!")
