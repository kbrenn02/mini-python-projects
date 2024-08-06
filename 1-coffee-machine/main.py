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