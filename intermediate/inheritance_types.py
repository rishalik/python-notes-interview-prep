# ===============================================
# PYTHON INTERMEDIATE: TYPES OF INHERITANCE
# ===============================================

# Inheritance defines how classes relate to one another. Python 
# supports multiple types of inheritance, allowing for complex 
# and reusable code structures.

# [VISUAL REPRESENTATION]
# Single:      A -> B
# Multiple:    A, B -> C
# Multilevel:  A -> B -> C
# Hierarchical:A -> B, A -> C



# --- 1. SINGLE INHERITANCE ---
# A child class inherits from a single parent class.
class Parent:
    def feature1(self):
        print("Feature 1 from Parent")

class Child(Parent):
    def feature2(self):
        print("Feature 2 from Child")


# --- 2. MULTIPLE INHERITANCE ---
# A child class inherits from more than one parent class.
class Father:
    def skill1(self):
        print("Driving skills from Father")

class Mother:
    def skill2(self):
        print("Cooking skills from Mother")

class Student(Father, Mother):
    def skill3(self):
        print("Studying skills from Student")


# --- 3. MULTILEVEL INHERITANCE ---
# A child class inherits from a parent, which in turn inherits 
# from another class (creating a "grandparent" relationship).
class Grandparent:
    def legacy(self):
        print("Family legacy")

class ParentLevel(Grandparent):
    def business(self):
        print("Family business")

class ChildLevel(ParentLevel):
    def hobby(self):
        print("Photography hobby")


# --- 4. HIERARCHICAL INHERITANCE ---
# Multiple child classes inherit from a single parent class.
class Vehicle:
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def drive(self):
        print("Driving the car")

class Bike(Vehicle):
    def ride(self):
        print("Riding the bike")


def main():
    print("--- Single Inheritance ---")
    obj1 = Child()
    obj1.feature1()
    obj1.feature2()

    print("\n--- Multiple Inheritance ---")
    obj2 = Student()
    obj2.skill1()
    obj2.skill2()

    print("\n--- Multilevel Inheritance ---")
    obj3 = ChildLevel()
    obj3.legacy()   # From Grandparent
    obj3.business() # From Parent
    obj3.hobby()    # From Child

    print("\n--- Hierarchical Inheritance ---")
    car = Car()
    bike = Bike()
    car.info()
    bike.info()

if __name__ == "__main__":
    main()