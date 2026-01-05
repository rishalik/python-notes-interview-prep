# ===============================================
# PYTHON INTERMEDIATE: INHERITANCE
# ===============================================

# Inheritance allows a 'Child' class to derive attributes and 
# methods from a 'Parent' class. This promotes code reusability 
# and creates a natural hierarchy.

# [CONCEPTUAL HIERARCHY]
#          [ Parent Class: Animal ]
#                   |
#         +---------+---------+
#         |                   |
# [ Child: Dog ]      [ Child: Cat ]
#  (Inherits Eat)      (Inherits Eat)
#  (Adds Bark)         (Adds Meow)



class Employee:
    """The Parent Class (Base Class)"""
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def show_identity(self):
        print(f"ID: {self.id_number} | Name: {self.name}")

    def work(self):
        print(f"{self.name} is performing general duties.")

class Developer(Employee):
    """The Child Class (Derived Class)"""
    def __init__(self, name, id_number, language):
        # super() calls the constructor of the Parent class (Employee)
        # This avoids re-writing the name and id_number logic
        super().__init__(name, id_number)
        self.language = language

    def work(self):
        """Method Overriding: Changing parent behavior for the child"""
        print(f"{self.name} is writing code in {self.language}.")

    def debug(self):
        """A method unique only to the Developer class"""
        print(f"{self.name} is fixing bugs...")

def main():
    print("--- 1. PARENT CLASS INSTANCE ---")
    generic_emp = Employee("John Doe", "E101")
    generic_emp.show_identity()
    generic_emp.work()

    print("\n--- 2. CHILD CLASS INSTANCE (Inheritance) ---")
    # Developer has access to show_identity() even though it's not defined in Developer
    dev = Developer("Charlie", "D502", "Python")
    dev.show_identity() 
    
    # Developer uses its own version of work() [Method Overriding]
    dev.work()
    
    # Developer can use its unique methods
    dev.debug()

    print("\n--- 3. VERIFYING RELATIONSHIP ---")
    print(f"Is 'dev' an Employee? {isinstance(dev, Employee)}")
    print(f"Is 'dev' a Developer? {isinstance(dev, Developer)}")

if __name__ == "__main__":
    main()