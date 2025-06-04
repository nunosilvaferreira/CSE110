def wind_chill(temp_f, wind_speed):
    """Calculate wind chill based on temperature (F) and wind speed (mph)."""
    return 35.74 + 0.6215 * temp_f - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp_f * (wind_speed ** 0.16)

def celsius_to_fahrenheit(temp_c):
    """Convert Celsius to Fahrenheit."""
    return temp_c * (9 / 5) + 32

def main():
    """Main function to interact with the user and compute wind chill values."""
    # Get user input
    temp = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()
    
    # Convert Celsius to Fahrenheit if necessary
    if unit == 'C':
        temp = celsius_to_fahrenheit(temp)
    
    print(f"\nWind Chill Calculations for {temp:.1f}F:\n")
    
    # Loop through wind speeds from 5 to 60 mph (incrementing by 5)
    for wind_speed in range(5, 65, 5):
        chill = wind_chill(temp, wind_speed)
        print(f"At temperature {temp:.1f}F, and wind speed {wind_speed} mph, the windchill is: {chill:.2f}F")

if __name__ == "__main__":
    main()
