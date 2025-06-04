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
sales_tax = subtotal * (tax_rate / 100)

# Calculate the total price (subtotal + sales tax)
total_price = subtotal + sales_tax

# Display sales tax and total price
print(f"Sales Tax: $ {sales_tax:.2f}")
print(f"Total (before tip): $ {total_price:.2f}")

# New Feature: Add a Tip
print("\nNew Feature: You can add a tip to your total if you'd like.")
tip_percentage = float(input("What percentage would you like to tip? (e.g., 10 for 10%): "))
tip_amount = total_price * (tip_percentage / 100)

# Calculate new total including tip
total_with_tip = total_price + tip_amount

# Display the tip and new total
print(f"Tip: $ {tip_amount:.2f}")
print(f"Total (including tip): $ {total_with_tip:.2f}")

# Input for the payment amount
payment_amount = float(input("\nWhat is the payment amount? $ "))

# Calculate the change
change = payment_amount - total_with_tip

# Display the change
print(f"Change: $ {change:.2f}")
