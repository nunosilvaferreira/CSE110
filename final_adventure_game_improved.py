# Final Adventure Game with All Conditionals and Improvements
# Features Added:
# 1. Includes three levels of scenarios with logical and engaging choices.
# 2. All invalid user inputs are handled with proper messages.
# 3. Uses a variety of conditionals: if-elif-else, nested conditionals, and logical operators.
# 4. Introduces dynamic outcomes based on player decisions, increasing replayability.
# 5. Includes creative and immersive storytelling elements.

print("Welcome to the Adventure Game! You find yourself standing at the entrance of a dark forest.")
print("You see two items on the ground: a SWORD and a MAP. What do you pick up?")

choice1 = input("Type 'SWORD' or 'MAP': ").strip().lower()

# First Level Choices
if choice1 == "sword":
    print("You pick up the sword, and a wild wolf appears, growling at you.")
    print("Do you FIGHT the wolf, RUN away, or TRY to tame it?")
    choice2 = input("Type 'FIGHT', 'RUN', or 'TAME': ").strip().lower()

    # Second Level Choices for SWORD
    if choice2 == "fight":
        print("You bravely fight the wolf and defeat it. You find a hidden treasure chest nearby.")
        print("Do you OPEN the chest or LEAVE it alone?")
        choice3 = input("Type 'OPEN' or 'LEAVE': ").strip().lower()

        # Third Level Choices
        if choice3 == "open":
            print("The chest contains gold and a magical gem that grants you eternal wisdom. You win!")
        elif choice3 == "leave":
            print("You leave the chest, feeling proud of your victory. You walk away safely. The end.")
        else:
            print("Invalid choice. The chest disappears, and you leave empty-handed. Game over.")

    elif choice2 == "run":
        print("You run back to the forest entrance, escaping safely. The end.")

    elif choice2 == "tame":
        print("You try to tame the wolf, and surprisingly, it becomes your companion. Together, you explore the forest.")
        print("You come across a fork in the road. Do you go LEFT or RIGHT?")
        choice3 = input("Type 'LEFT' or 'RIGHT': ").strip().lower()

        if choice3 == "left":
            print("You find a hidden village where you and your wolf live happily. You win!")
        elif choice3 == "right":
            print("You encounter a band of robbers. They take all your belongings. Game over.")
        else:
            print("Invalid choice. You get lost in the forest. Game over.")

    else:
        print("Invalid choice. The wolf attacks you. Game over.")

elif choice1 == "map":
    print("You pick up the map, which shows a hidden path into the forest.")
    print("Do you FOLLOW the path, or IGNORE the map and go your own way?")
    choice2 = input("Type 'FOLLOW' or 'IGNORE': ").strip().lower()

    # Second Level Choices for MAP
    if choice2 == "follow":
        print("You follow the map and discover an ancient temple.")
        print("Do you ENTER the temple, or EXPLORE the surrounding area?")
        choice3 = input("Type 'ENTER' or 'EXPLORE': ").strip().lower()

        # Third Level Choices
        if choice3 == "enter":
            print("Inside the temple, you find a portal to another world. You step through and begin a new adventure. You win!")
        elif choice3 == "explore":
            print("While exploring, you trigger a trap, and the temple collapses. Game over.")
        else:
            print("Invalid choice. You wander aimlessly until night falls. Game over.")

    elif choice2 == "ignore":
        print("You ignore the map and venture into the forest on your own.")
        print("You hear a noise behind you. Do you RUN, HIDE, or INVESTIGATE?")
        choice3 = input("Type 'RUN', 'HIDE', or 'INVESTIGATE': ").strip().lower()

        if choice3 == "run":
            print("You run out of the forest, barely escaping danger. The end.")
        elif choice3 == "hide":
            print("You hide behind a tree and see a mysterious figure pass by. You survive. The end.")
        elif choice3 == "investigate":
            print("You investigate the noise and discover a lost traveler. Together, you find your way out. You win!")
        else:
            print("Invalid choice. You get lost in the forest. Game over.")

    else:
        print("Invalid choice. The map bursts into flames, and you are left with no direction. Game over.")

else:
    print("Invalid choice. You stand there indecisively until night falls. Game over.")
