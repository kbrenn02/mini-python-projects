class MenuItem:
    # Models each Menu Item.
    # This is how you define an object of the class. If parameters are passed in, assign them to the self.
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    # Models the Menu with drinks.
    # The Menu class calls on the MenuItem class above to initialize the 3 menu items
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]


    # Returns all the names of the available menu items by calling on the self.menu in the initialization
    # A function in a Class is called a method, so this is the get_items method
    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    

    # Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None
    # This compares the user's order to the list of items in the menu
    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")