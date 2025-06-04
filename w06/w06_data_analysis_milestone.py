# Open the dataset file
with open("life-expectancy.csv", "r") as file:
    next(file)  # Skip the header row
    min_life_expectancy = float("inf")  # Initialize to a high number
    max_life_expectancy = float("-inf")  # Initialize to a low number

    # Read and process each line
    for line in file:
        parts = line.strip().split(",")  # Split each line by commas
        life_expectancy = float(parts[3])  # Extract life expectancy column (index may vary)

        # Update min and max life expectancy values
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy

# Display the results
print(f"The lowest life expectancy in the dataset is: {min_life_expectancy}")
print(f"The highest life expectancy in the dataset is: {max_life_expectancy}")
