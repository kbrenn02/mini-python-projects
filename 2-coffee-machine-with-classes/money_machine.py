class MoneyMachine:
    # All caps for global variables that you don't want to change
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }


    # define the attributes of the MoneyMachine class. By doing this, we can call/print the profit and money_received attributes
    def __init__(self):
        self.profit = 0
        self.money_received = 0


    # Prints the current profit
    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")


    # Returns the total calculated from coins inserted
    def process_coins(self):
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received


    # Returns True when payment is accepted, or False if insufficient
    def make_payment(self, cost):
        # Able to call on methods in the same class their defined by using self.method()
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
