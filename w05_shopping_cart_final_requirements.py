cart_items = []  # List to store item names
cart_prices = []  # List to store item prices
cart_quantities = []  # List to store item quantities

def display_cart():
    print("\nThe contents of the shopping cart are:")
    if not cart_items:
        print("Your cart is empty.")
    else:
        for i, (item, price, quantity) in enumerate(zip(cart_items, cart_prices, cart_quantities), start=1):
            print(f"{i}. {item} (x{quantity}) - ${price:.2f} each - Total: ${price * quantity:.2f}")

print("Welcome to the Shopping Cart Program!")

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Apply discount")
    print("6. Quit")
    
    choice = input("Please enter an action: ")
    
    if choice == "1":
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))
        quantity = int(input(f"How many '{item}' would you like to add? "))
        cart_items.append(item)
        cart_prices.append(price)
        cart_quantities.append(quantity)
        print(f"{quantity} '{item}' has been added to the cart.")
    
    elif choice == "2":
        display_cart()
    
    elif choice == "3":
        display_cart()
        
        try:
            remove_index = int(input("Which item would you like to remove? ")) - 1
            if 0 <= remove_index < len(cart_items):
                removed_item = cart_items.pop(remove_index)
                cart_prices.pop(remove_index)
                cart_quantities.pop(remove_index)
                print(f"'{removed_item}' has been removed from the cart.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice == "4":
        total = sum(price * quantity for price, quantity in zip(cart_prices, cart_quantities))
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    
    elif choice == "5":
        discount_code = input("Enter discount code (SAVE10 for 10% off): ")
        if discount_code == "SAVE10":
            total = sum(price * quantity for price, quantity in zip(cart_prices, cart_quantities))
            discount = total * 0.10
            total -= discount
            print(f"Discount applied! You saved ${discount:.2f}.")
            print(f"New total: ${total:.2f}")
        else:
            print("Invalid discount code.")
    
    elif choice == "6":
        print("Thank you for shopping with us. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")
