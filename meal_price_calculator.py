# Input for meal prices
child_meal_price = float(input("What is the price of a child's meal? $ "))
adult_meal_price = float(input("What is the price of an adult's meal? $ "))

# Input for the number of meals
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Calculate the subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

# Display the subtotal
print(f"\nSubtotal: $ {subtotal:.2f}")
