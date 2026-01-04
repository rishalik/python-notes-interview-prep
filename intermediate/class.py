# ===============================================
# PYTHON FUNDAMENTALS: CLASSES AND OBJECTS (OOP)
# ===============================================

# Classes are blueprints for creating objects. Objects are 
# instances of a class that encapsulate data and behavior.

# [OOP CONCEPT]
#   CLASS (Blueprint) ---------> OBJECT (The Build)
#   "Car Design"                 "Your Specific Porsche"
#   - color                      - color = "Silver"
#   - engine_type                - engine_type = "Electric"

class Car:
    # Class Attribute: Shared by all instances
    wheels = 4

    def __init__(self, brand, model, year):
        """
        The Constructor (__init__) initializes the object's attributes.
        'self' represents the specific instance being created.
        """
        self.brand = brand   # Instance Attribute
        self.model = model   # Instance Attribute
        self.year = year     # Instance Attribute
        self.engine_on = False

    def start_engine(self):
        """A method representing a behavior of the object."""
        self.engine_on = True
        return f"The {self.brand} {self.model}'s engine is now roaring!"

    def get_description(self):
        return f"{self.year} {self.brand} {self.model}"

def main():
    # Creating instances (Objects) of the Car class
    car1 = Car("Porsche", "911 Carrera", 2024)
    car2 = Car("Tesla", "Model S", 2023)

    print(f"Car 1: {car1.get_description()}")
    print(car1.start_engine())

    print(f"\nCar 2: {car2.get_description()}")
    print(f"Engine Status: {'Running' if car2.engine_on else 'Off'}")

    # Accessing class attributes
    print(f"\nAll cars have {Car.wheels} wheels.")

if __name__ == "__main__":
    main()