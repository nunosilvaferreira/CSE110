# Open the dataset file
with open("life-expectancy.csv", "r") as file:
    next(file)  # Skip header row

    # Initialize variables
    overall_min_life = float("inf")
    overall_max_life = float("-inf")
    min_country = max_country = ""
    min_year = max_year = ""

    data = []  # Store data for later analysis

    # Read and process each line
    for line in file:
        parts = line.strip().split(",")  # Split by commas
        country, code, year, life_expectancy = parts[0], parts[1], int(parts[2]), float(parts[3])

        # Store data in a list for later use
        data.append((country, code, year, life_expectancy))

        # Find overall min and max life expectancy
        if life_expectancy < overall_min_life:
            overall_min_life, min_country, min_year = life_expectancy, country, year
        if life_expectancy > overall_max_life:
            overall_max_life, max_country, max_year = life_expectancy, country, year

# Display overall min and max life expectancy
print(f"\nThe overall max life expectancy is: {overall_max_life:.2f} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {overall_min_life:.2f} from {min_country} in {min_year}")

# User Input for Year Analysis
year_input = int(input("\nEnter the year of interest: "))

year_life_expectancies = [life for (country, code, year, life) in data if year == year_input]

if year_life_expectancies:
    avg_life = sum(year_life_expectancies) / len(year_life_expectancies)

    min_life = min(year_life_expectancies)
    max_life = max(year_life_expectancies)

    min_country = next(country for (country, code, year, life) in data if year == year_input and life == min_life)
    max_country = next(country for (country, code, year, life) in data if year == year_input and life == max_life)

    print(f"\nFor the year {year_input}:")
    print(f"The average life expectancy across all countries was {avg_life:.2f}")
    print(f"The max life expectancy was in {max_country} with {max_life:.2f}")
    print(f"The min life expectancy was in {min_country} with {min_life:.2f}")
else:
    print(f"\nNo data available for the year {year_input}")

# User Input for Country Analysis
country_input = input("\nEnter a country to analyze: ").strip().title()

country_life_expectancies = [life for (country, code, year, life) in data if country == country_input]

if country_life_expectancies:
    avg_country_life = sum(country_life_expectancies) / len(country_life_expectancies)
    min_country_life = min(country_life_expectancies)
    max_country_life = max(country_life_expectancies)

    print(f"\nFor {country_input}:")
    print(f"The average life expectancy was {avg_country_life:.2f}")
    print(f"The max life expectancy was {max_country_life:.2f}")
    print(f"The min life expectancy was {min_country_life:.2f}")
else:
    print(f"\nNo data available for {country_input}")
