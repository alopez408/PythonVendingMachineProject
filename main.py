class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class VendingMachine:
    def __init__(self):
        self.beverages = [
            Beverage("Cocoa Cola", 3.25),
            Beverage("Pepsi", 3.25),
            Beverage("Sprite", 3.25),
            Beverage("Mt. Dew", 3.25),
            Beverage("Monster", 4.50),
            Beverage("Saratoga Water", 10.00)
        ]

    def display_menu(self):
        print("\n--- Beverage Menu ---")
        for idx, bev in enumerate(self.beverages):
            print(f"{idx + 1}. {bev}")
        print("---------------------")

    def vend_beverage(self, choice, money_inserted):
        if choice < 1 or choice > len(self.beverages):
            print("Invalid selection. Please try again.")
            return money_inserted # Return money back
        beverage = self.beverages[choice - 1]
        if money_inserted < beverage.price:
            print(f"Insufficient funds. {beverage.name} cost ${beverage.price:.2f}. You inserted ${money_inserted:.2f}.")
            print("Please insert more money.")
            return money_inserted # Keep the money inserted so far
        change = money_inserted - beverage.price
        print(f"Vending {beverage.name}... Enjoy!")
        if change > 0:
            print(f"Returning change: ${change:.2f}")
        return 0 # Money reset after vending

    def run(self):
        print("Welcome to the Vending Machine!")
        while True:
            self.display_menu()
            try:
                choice = int(input("Select a beverage (1-6): "))
                money = float(input("Insert money: $"))
                remaining_money = self.vend_beverage(choice, money)
                while remaining_money > 0:
                    more_money = float(input("Insert additional money: $"))
                    remaining_money += more_money
                    remaining_money = self.vend_beverage(choice, remaining_money)
            except ValueError:
                print("Invalid input. Please enter numbers only.")

# Start the vending machine
if __name__ == "__main__":
    machine = VendingMachine()
    machine.run()
