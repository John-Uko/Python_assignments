# Assignment 1: Design Your Own Class

class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")
    
    def browse(self, website):
        print(f"{self.brand} {self.model} is browsing {website}... 🌐")

# Inheritance Example
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu):
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu
    
    def play_game(self, game):
        print(f"{self.brand} {self.model} with {self.gpu} is playing {game}! 🎮")


# Create objects
phone1 = Smartphone("Apple", "iPhone 14", "128GB", "20 hours")
phone2 = GamingSmartphone("Asus", "ROG Phone 6", "256GB", "24 hours", "Adreno 730")

phone1.call("08012345678")
phone2.browse("https://openai.com")
phone2.play_game("Call of Duty Mobile")


