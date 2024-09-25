import data
import sandwich_maker
import cashier

# Create variables for resources and recipes
resources = data.resources
recipes = data.recipes

# Create instances of the SandwichMaker and Cashier classes
machine = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()


def order_sandwich():
    while True:
        print("What size sandwich would you like? (small/ medium/ large/ off/ report): ")
        choice = input().lower()

        if choice in ["small", "medium", "large"]:
            # Get the order ingredients and cost based on the user's choice
            order_ingredients = recipes[choice]["ingredients"]
            cost = recipes[choice]["cost"]

            # Check if resources are sufficient
            if machine.check_resources(order_ingredients):
                print(f"The cost for the {choice.capitalize()} sandwich is: ${cost}")

                # Ask the user to insert coins
                print("Please insert coins.")
                coins = cashier_instance.process_coins()

                # Check if the transaction is successful
                if cashier_instance.transaction_result(coins, cost):
                    # Make the sandwich
                    machine.make_sandwich(choice, order_ingredients)

        elif choice == "off":
            print("Shutting down the machine.")
            break

        elif choice == "report":
            # Print a report of the remaining resources
            for ingredient, quantity in machine.machine_resources.items():
                unit = "slice(s)" if ingredient != "cheese" else "ounce(s)"
                print(f'{ingredient.capitalize()}: {quantity} {unit}')
        else:
            print("Invalid input. Please choose from small, medium, large, off, or report.")


def main():
    # Call the order_sandwich function within main
    order_sandwich()


if __name__ == "__main__":
    main()
