# Base class Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def display_details(self):
        print(f"Smartphone Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Life: {self.battery_life} hours")

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def use_app(self, app_name):
        print(f"Using {app_name} on {self.brand} {self.model}...")

# Inheritance: subclass for a more specific type of Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, gaming_features):
        super().__init__(brand, model, battery_life)
        self.gaming_features = gaming_features  # special features for gaming

    def display_details(self):
        super().display_details()  # Call the parent method
        print(f"Gaming Features: {self.gaming_features}")

    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.brand} {self.model} with {self.gaming_features}...")

# Create an object of the base class
phone1 = Smartphone("Apple", "iPhone 13", 20)
phone1.display_details()
phone1.call("123-456-7890")

# Create an object of the subclass
gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 16, "6GB RAM + 144Hz Display")
gaming_phone.display_details()
gaming_phone.play_game("PUBG Mobile")
