from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Don't call classes directly into code. Need to assign them to an object, then you can use them
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
still_ordering = True


while still_ordering:
    # Access the menu items, then display them in the input call
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) or say goodbye: ").lower()

    # End the loop if the customer asked to leave
    if choice == "off" or choice == "goodbye" or choice == "good bye" or choice == "good-bye":
        still_ordering = False
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        # By doing this, the drink now has all the attributes defined in menu (name, water, milk, coffee, cost)
        drink = menu.find_drink(choice)
        # Checking for sufficient resources and sufficient payment
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

