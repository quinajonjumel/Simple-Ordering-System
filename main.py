class OrderSystem:
    def __init__(self):
        self.menu = {"Burger": 5.00, "Pizza": 8.00, "Salad": 4.50, "Drink": 1.50}
        self.order = {}

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")

    def take_order(self):
        while True:
            item = input("Enter the item you want to order (or 'done' to finish): ").capitalize()

            if item == 'Done':
                break

            if item in self.menu:
                quantity = int(input(f"How many {item}s do you want to order? "))
                if item in self.order:
                    self.order[item] += quantity
                else:
                    self.order[item] = quantity
                print(f"{quantity} {item}(s) added to your order.")
            else:
                print("Invalid item. Please choose from the menu.")

    def calculate_total(self):
        total = sum(self.menu[item] * quantity for item, quantity in self.order.items())
        return total

    def display_order_summary(self):
        print("\nOrder Summary:")
        for item, quantity in self.order.items():
            print(f"{item}: {quantity} x ${self.menu[item]:.2f} = ${quantity * self.menu[item]:.2f}")

        total = self.calculate_total()
        print(f"\nTotal: ${total:.2f}")

    def start_ordering(self):
        print("Welcome to the Simple Ordering System!")
        self.display_menu()
        self.take_order()
        self.display_order_summary()
        print("Thank you for ordering!")

# Usage
order_system = OrderSystem()
order_system.start_ordering()
