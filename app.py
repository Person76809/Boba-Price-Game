print("Welcome to the Boba Tea Ordering Game!")

# Define a dictionary of boba tea flavors and prices
flavors = {
    "Classic Milk Tea": 4.50,
    "Taro Milk Tea": 5.00,
    "Strawberry Green Tea": 4.75,
    "Honeydew Milk Tea": 4.75,
    "Thai Tea": 5.50
}

# Ask the player which flavor they want
print("Here are the available flavors:")
for flavor in flavors:
    print("- " + flavor)

chosen_flavor = input("Which flavor would you like? ")

# Check if the chosen flavor is valid
if chosen_flavor not in flavors:
    print("Sorry, that's not a valid flavor.")
else:
    # Ask the player how many cups they want
    num_cups = int(input("How many cups of " + chosen_flavor + " would you like? "))

    # Calculate the total cost
    cost_per_cup = flavors[chosen_flavor]
    total_cost = num_cups * cost_per_cup

    # Display the order and total cost
    print("Your order is:")
    print("- " + str(num_cups) + " cups of " + chosen_flavor)
    print("Your total cost is: $" + str(total_cost))
