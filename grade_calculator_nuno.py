# Ask the user for their grade percentage
grade_percentage = int(input("Enter your grade percentage: "))

# Determine the letter grade
if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"

# Determine if the user passed or failed
if grade_percentage >= 70:
    print("Congratulations, you passed the class!")
else:
    print("Don't give up! Keep trying and you'll improve next time.")

# Add a "+" or "-" sign to the grade, where applicable
if letter != "F":  # F grades don't get a "+" or "-"
    last_digit = grade_percentage % 10  # Get the last digit of the percentage

    if last_digit >= 7:
        sign = "+"
    elif last_digit < 3:
        sign = "-"
    else:
        sign = ""
else:
    sign = ""  # No "+" or "-" for F grades

# Handle special cases for A and F grades
if letter == "A" and sign == "+":
    sign = ""  # No A+ grade
elif letter == "F":
    sign = ""  # No F+ or F-

# Display the final grade
print(f"Your letter grade is: {letter}{sign}")
