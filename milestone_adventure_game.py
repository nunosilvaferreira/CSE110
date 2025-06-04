# Milestone Submission for Text-Based Adventure Game
# This program includes the first scenario with possible choices and follow-up responses.
# Design Plan:
# 1. The game will include three levels of scenarios with different choices leading to distinct outcomes.
# 2. One level will include more than two choices.
# 3. Creativity will be shown by including a hidden path triggered by a secret word.

def main():
    print("You find yourself at the edge of a mysterious forest. You see two items on the ground: a SWORD and a MAP. Which one do you pick up?")
    choice = input("Type 'SWORD' or 'MAP': ").strip().lower()

    if choice == "sword":
        print("You pick up the sword, and suddenly, a wild wolf appears in front of you. Do you want to FIGHT or RUN?")
    elif choice == "map":
        print("You pick up the map and discover a hidden path leading deeper into the forest. Do you want to FOLLOW the path or GO BACK?")
    else:
        print("That's not a valid choice. Please type 'SWORD' or 'MAP'.")

# Run the game
if __name__ == "__main__":
    main()
