# Define the menu items, how much they cost, and how much of each ingredient they take. This is best done in a dictionary
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


# Define the amount of resources we have to use. These numbers will change, hence the name is in all lowercase
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# Checks if there is enough resources to make the desired drink
def check_ingredients(drink, resources):
    # If the value of water needed to make the drink is greater than our water resource, show that as an alert. Do that for all ingredients
    if drink["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water.")
    elif drink["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
    elif drink["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk.")
    else:
        # If we have enough of all ingredients, no error is displayed and the transaction continues to the next step
        return True
    

# Format resources into printable format
def format_resources(resources):
    # Because resource amounts change, by calling the resources['water'], this should dynamically render the remaining ingredients
    water_amount = resources["water"]
    milk_amount = resources["milk"]
    coffee_amount = resources["coffee"]
    money_amount = resources["money"]
    return f"Water: {water_amount}ml \nMilk: {milk_amount}ml \nCoffee: {coffee_amount}g \nMoney: ${money_amount}"


# Returns the total from coins inserted
def process_coins(q, d, n, p):
    # Totals up how much the customer paid
    return (q * .25) + (d * .10) + (n * .05) + (p * .01)


# Create a while loop so the user can keep ordering until they say goodbye
still_ordering = True
while still_ordering:
    # Take the customer's original input and put it in a consistent format
    order = input("What would you like? (espresso/latte/cappuccino) or say goodbye: ").lower()

    # Immediately end the loop if the customer leaves (this is also the first thing that happens after they finish ordering
    # the first drink because of the loop)
    if order == "off" or order == "goodbye" or order == "good bye" or order == "good-bye":
        still_ordering = False

    # This is a command for the employee side to check how many ingredients are left
    if order == "report":
        print(format_resources(resources))

    # If the customer orders a valid drink, define a variable for that drink that we can work with and access from the Menu
    if order == "espresso" or order == "latte" or order == "cappuccino":
        drink = MENU[order]

        # Check if we have enough ingredients to make the drink. It will return true or false. If true, the next block runs
        checking = check_ingredients(drink, resources)
        if checking:
            # Reduce the resources dictionary by the amount used to make the drink. This nesting is how the ingredients for each
            # drink is accessed in a nested dictionary
            resources["water"] -= drink["ingredients"]["water"]
            resources["coffee"] -= drink["ingredients"]["coffee"]
            resources["milk"] -= drink["ingredients"]["milk"]
        
        # After the resources are updated in the backend, then we take the payment. Payment in coins. Gather input from customer
        print("Please insert coins.")
        # Convert input (which comes as a string) immediately into a string to work with
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickles = int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))
        # Using the process_coins function, get the total for what the customer paid
        total_paid = process_coins(quarters, dimes, nickles, pennies)

        # Series of moves to take depending on how much the customer paid
        if total_paid < drink["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
        elif total_paid == drink["cost"]:
            resources["money"] += drink["cost"]
            print(f"Here is you {order}. Enjoy!")
        elif total_paid > drink["cost"]:
            resources["money"] += drink["cost"]
            refund = round(total_paid - drink["cost"], 2)
            print(f"Here is ${refund} in change.")
            print(f"Here is you {order}. Enjoy!")