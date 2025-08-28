# Base class: Superhero
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, with the power of {self.power}, protecting {self.city}!")

# Inherited class: FlyingHero (demonstrates inheritance & encapsulation)
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.__flight_speed = flight_speed  # Encapsulated attribute

    def fly(self):
        print(f"{self.name} is flying at {self.__flight_speed} km/h!")

    def get_flight_speed(self):
        return self.__flight_speed

# Create superhero objects
hero1 = Superhero("Shadow", "Invisibility", "Gotham")
hero2 = FlyingHero("Skyblade", "Flight & Strength", "Metro City", 300)

hero1.introduce()
hero2.introduce()
hero2.fly()
print("Flight speed:", hero2.get_flight_speed(), "km/h")
