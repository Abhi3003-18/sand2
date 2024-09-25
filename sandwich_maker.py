class SandwichMaker:
    def __init__(self, resources):
        self.resources = resources  # This stores the machine's resources

    def check_resources(self, ingredients):
        """Returns True when the order can be made, False if ingredients are insufficient."""
        for ingredient, quantity in ingredients.items():
            if self.resources.get(ingredient, 0) < quantity:  # Use self.resources
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for ingredient, quantity in order_ingredients.items():
            self.resources[ingredient] -= quantity  # Use self.resources
        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")
