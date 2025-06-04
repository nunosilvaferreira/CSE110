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

# Input for the sales tax rate
tax_rate = float(input("What is the sales tax rate? (e.g., 6 for 6%): "))

# Calculate sales tax
sales_tax = subtotal * (tax_rate / 100)

# Calculate the total price
total_price = subtotal + sales_tax

# Display sales tax and total price
print(f"Sales Tax: $ {sales_tax:.2f}")
print(f"Total: $ {total_price:.2f}")

# Input for the payment amount
payment_amount = float(input("\nWhat is the payment amount? $ "))

# Calculate the change
change = payment_amount - total_price

# Display the change
print(f"Change: $ {change:.2f}")
