# Final Submission for Text-Based Adventure Game
# Features Added:
# 1. The game includes three levels of scenarios with multiple distinct choices.
# 2. One level has more than two choices, adding variety.
# 3. A hidden path is triggered by entering a secret keyword ("SECRET").
# 4. A randomized event system is added after the first choice, introducing unpredictability.
# 5. Invalid inputs are handled at every level with appropriate messages.
# 6. The randomized event ensures that no two playthroughs are exactly alike.

import random

def main():
    print("You find yourself at the edge of a mysterious forest. You see two items on the ground: a SWORD and a MAP. Which one do you pick up?")
    choice1 = input("Type 'SWORD', 'MAP', or 'SECRET': ").strip().lower()

    # Randomized Event System
    def random_event():
        events = [
            "A sudden storm rolls in, and lightning strikes a nearby tree!",
            "You hear eerie whispers coming from the shadows.",
            "A friendly rabbit hops by, carrying a shiny key.",
            "The ground shakes violently as if something massive is approaching."
        ]
        return random.choice(events)

    if choice1 == "sword":
        print("You pick up the sword, and suddenly, a wild wolf appears in front of you.")
        print(random_event())  # Introduce random event here
        print("Do you want to FIGHT or RUN?")
        choice2 = input("Type 'FIGHT' or 'RUN': ").strip().lower()

        if choice2 == "fight":
            print("You fight bravely and defeat the wolf. You find a hidden treasure chest. Do you OPEN it or LEAVE it?")
            choice3 = input("Type 'OPEN' or 'LEAVE': ").strip().lower()

            if choice3 == "open":
                print("The chest contains a magical gem that grants you eternal wisdom. You win!")
            elif choice3 == "leave":
                print("You leave the chest and walk away, forever wondering what could have been. The end.")
            else:
                print("That's not a valid choice. The wolf comes back and chases you away. Game over.")

        elif choice2 == "run":
            print("You run back to the forest's edge and escape safely. The end.")
        else:
            print("That's not a valid choice. The wolf attacks you. Game over.")

    elif choice1 == "map":
        print("You pick up the map and discover a hidden path leading deeper into the forest.")
        print(random_event())  # Introduce random event here
        print("Do you want to FOLLOW the path or GO BACK?")
        choice2 = input("Type 'FOLLOW' or 'GO BACK': ").strip().lower()

        if choice2 == "follow":
            print("You follow the path and find an ancient temple. Do you ENTER it or EXPLORE the area?")
            choice3 = input("Type 'ENTER' or 'EXPLORE': ").strip().lower()

            if choice3 == "enter":
                print("Inside the temple, you find a portal to another world. You step through and begin a new adventure. You win!")
            elif choice3 == "explore":
                print("While exploring, you trigger a trap and the temple collapses. Game over.")
            else:
                print("That's not a valid choice. You get lost in the forest. Game over.")

        elif choice2 == "go back":
            print("You decide to play it safe and go back to the forest's edge. The end.")
        else:
            print("That's not a valid choice. You get lost in the forest. Game over.")

    elif choice1 == "secret":
        print("You have unlocked a hidden path by discovering the secret word!")
        print("A hidden staircase appears, leading you to a magical artifact. You are teleported to safety. You win!")
    else:
        print("That's not a valid choice. The forest swallows you whole. Game over.")

# Run the game
if __name__ == "__main__":
    main()
