# ===============================================
# PYTHON FUNDAMENTALS: VARIABLES EXPLANATION
# ===============================================

# --- SECTION 1: VARIABLE FUNDAMENTALS ---

# A variable is a named location in memory used to store data.
# Python is dynamically typed, meaning the type of the variable is determined 
# by the value assigned, and does not need to be declared beforehand.

# 1.1 Creating and Assigning Variables
print("--- 1.1: Basic Variable Assignment ---")

# Assignment is done using the equals sign (=)
age = 30           # Integer type
name = "Alice"     # String type
is_student = True  # Boolean type

print(f"Variable 'age' stores: {age}")
print(f"Variable 'name' stores: {name}")
print(f"Variable 'is_student' stores: {is_student}")

# We can check the type of a variable using the type() function
print(f"Type of 'age': {type(age)}")
print(f"Type of 'name': {type(name)}")


# 1.2 Variable Naming Rules and Conventions
print("\n--- 1.2: Naming Rules Examples ---")

# Valid names:
user_id = 101       # Standard snake_case convention
_temp_value = 5.5   # Starts with an underscore
MaximumValue = 500  # Capital letters are fine

# Invalid names (would cause a SyntaxError if uncommented):
# 2nd_data = "Error"
# user-name = "Error"
# if = 7  # 'if' is a reserved keyword

print(f"Valid name example (user_id): {user_id}")


# 1.3 Reassignment (Dynamic Typing)
print("\n--- 1.3: Reassignment Example ---")

x = 10         # x is initially an integer
print(f"x initial value and type: {x}, {type(x)}")

x = 20.5       # The variable x is reassigned a new value and type (float)
print(f"x reassigned (float): {x}, {type(x)}")

x = "Hello"    # x is reassigned a string value and type
print(f"x reassigned (string): {x}, {type(x)}")


# 1.4 Multiple Assignment
print("\n--- 1.4: Multiple Assignment ---")

# Assign the same value to three variables
a = b = c = 5
print(f"a, b, c (same value): {a}, {b}, {c}")

# Assign different values to three variables (Tuple Unpacking)
item_name, quantity, price = "Book", 2, 19.99
print(f"Item: {item_name}, Quantity: {quantity}, Price: {price}")


# --- SECTION 2: VARIABLE SCOPE (Brief Introduction) ---
print("\n--- 2. Variable Scope Example ---")

global_message = "I exist everywhere"  # Global variable

def show_scope():
    local_number = 100  # Local variable (only exists inside this function)
    print(f"Inside function: {global_message}")
    print(f"Inside function: {local_number}")

show_scope()
print(f"Outside function: {global_message}")

# The line below would cause an error because local_number is out of scope:
# print(local_number)