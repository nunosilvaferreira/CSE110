# Life Expectancy Data Analysis Program
# This program reads life expectancy data from a CSV file and allows the user to analyze it in different ways.

filename = "life-expectancy.csv"

data = []
# Open the file and read the data, skipping the header row
with open(filename, "r") as file:
    next(file)  # Skip header row
    for line in file:
        parts = line.strip().split(",")
        country, year, life_expectancy = parts[0], int(parts[2]), float(parts[3])
        data.append((country, year, life_expectancy))

# Menu-driven interface for user interaction
while True:
    print("\nMenu:")
    print("1. View overall min/max life expectancy")
    print("2. Analyze a specific year")
    print("3. Analyze a specific country")
    print("4. Find the largest drop in life expectancy")
    print("5. Visualize life expectancy for a year")
    print("6. Exit")

    choice = input("Choose an option: ")
    
    if choice == "1":
        # Find overall min and max life expectancy
        min_life = min(data, key=lambda x: x[2])
        max_life = max(data, key=lambda x: x[2])
        print(f"\nThe overall max life expectancy is: {max_life[2]:.2f} from {max_life[0]} in {max_life[1]}")
        print(f"The overall min life expectancy is: {min_life[2]:.2f} from {min_life[0]} in {min_life[1]}")
    
    elif choice == "2":
        # Analyze life expectancy for a specific year
        year = int(input("Enter a year: "))
        year_data = [entry for entry in data if entry[1] == year]
        if year_data:
            avg_life = sum(entry[2] for entry in year_data) / len(year_data)
            min_life = min(year_data, key=lambda x: x[2])
            max_life = max(year_data, key=lambda x: x[2])
            print(f"\nFor the year {year}:")
            print(f"The average life expectancy across all countries was {avg_life:.2f}")
            print(f"The max life expectancy was in {max_life[0]} with {max_life[2]:.2f}")
            print(f"The min life expectancy was in {min_life[0]} with {min_life[2]:.2f}")
        else:
            print("No data available for this year.")
    
    elif choice == "3":
        # Analyze life expectancy for a specific country
        country = input("Enter a country: ")
        country_data = [entry for entry in data if entry[0].lower() == country.lower()]
        if country_data:
            avg_life = sum(entry[2] for entry in country_data) / len(country_data)
            min_life = min(country_data, key=lambda x: x[2])
            max_life = max(country_data, key=lambda x: x[2])
            print(f"\nFor {country}:")
            print(f"The average life expectancy was {avg_life:.2f}")
            print(f"The max life expectancy was {max_life[2]:.2f}")
            print(f"The min life expectancy was {min_life[2]:.2f}")
        else:
            print("No data available for this country.")
    
    elif choice == "4":
        # Find the largest drop in life expectancy for any country
        data.sort()
        largest_drop = (None, 0, 0, float('-inf'))
        for i in range(len(data) - 1):
            country1, year1, life1 = data[i]
            country2, year2, life2 = data[i + 1]
            if country1 == country2 and year2 == year1 + 1:
                drop = life1 - life2
                if drop > largest_drop[3]:
                    largest_drop = (country1, year1, year2, drop)
        print(f"\nThe largest drop in life expectancy was in {largest_drop[0]} from {largest_drop[1]} to {largest_drop[2]}, with a drop of {largest_drop[3]:.2f} years.")
    
    elif choice == "5":
        # Visualize life expectancy for a specific year using ASCII bar chart
        year = int(input("Enter a year: "))
        year_data = [entry for entry in data if entry[1] == year]
        if year_data:
            print(f"\nLife Expectancy in {year}:")
            for country, _, life in sorted(year_data, key=lambda x: x[2], reverse=True)[:10]:
                print(f"{country:15} {'*' * int(life)} ({life:.2f})")
        else:
            print("No data available for this year.")
    
    elif choice == "6":
        # Exit the program
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice. Please try again.")
