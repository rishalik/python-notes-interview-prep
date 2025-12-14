# ===============================================
# PYTHON FUNDAMENTALS: DATA TYPES EXPLANATION
# ===============================================

# Data types classify the kind of value a variable holds, defining
# how the data is stored and what operations can be performed on it.

# --- 1. NUMERIC TYPES (int, float, complex) ---
print("\n--- 1. NUMERIC TYPES ---")

# INT: Whole numbers (no decimal point).
int_num = 100
# FLOAT: Numbers with a decimal point.
float_num = 10.5
# COMPLEX: Numbers with an imaginary part (j).
complex_num = 4 + 7j

print(f"Integer ({type(int_num)}): {int_num}")
print(f"Float ({type(float_num)}): {float_num}")
print(f"Complex ({type(complex_num)}): {complex_num}")

# --- 2. TEXT TYPE (str) ---
print("\n--- 2. TEXT TYPE ---")

# STR: Sequence of characters enclosed in quotes. Strings are immutable.
my_string = "Python Data Types"

print(f"String ({type(my_string)}): '{my_string}'")
# Accessing characters by index (0-based)
print(f"First character: {my_string[0]}")
# Length of the string
print(f"Length: {len(my_string)}")

# --- 3. SEQUENCE TYPES (list, tuple) ---
print("\n--- 3. SEQUENCE TYPES ---")

# LIST: Ordered, mutable (changeable) collection, allows duplicates. Defined with [].
my_list = [10, "A", 3.14]
print(f"Original List ({type(my_list)}): {my_list}")

# Lists are MUTABLE: change an element
my_list[0] = 50
my_list.append("New")
print(f"Modified List: {my_list}")

# TUPLE: Ordered, immutable (unchangeable) collection, allows duplicates. Defined with ().
my_tuple = (1, 2, "three")
print(f"Tuple ({type(my_tuple)}): {my_tuple}")

# Attempting to change a tuple element will result in a TypeError:
# my_tuple[0] = 50  # Uncommenting this line causes an error

# RANGE: Represents an immutable sequence of numbers (often used in loops).
my_range = range(5)  # Generates numbers 0, 1, 2, 3, 4
print(f"Range Type ({type(my_range)}): {list(my_range)}") # Convert to list for printing

# --- 4. MAPPING TYPE (dict) ---
print("\n--- 4. MAPPING TYPE ---")

# DICT: Ordered (Python 3.7+), changeable, collection of KEY-VALUE pairs. Defined with {}.
person = {"name": "Eve", "age": 22, "is_admin": False}
print(f"Dictionary ({type(person)}): {person}")

# Accessing a value by its key
print(f"Value for 'name': {person['name']}")

# Dictionaries are MUTABLE: change a value
person["age"] = 23
print(f"Modified Age: {person['age']}")

# --- 5. SET TYPES (set, frozenset) ---
print("\n--- 5. SET TYPES ---")

# SET: Unordered, unindexed, changeable, and does NOT allow duplicate members. Defined with {}.
basket = {"apple", "banana", "apple", "cherry"}
print(f"Set ({type(basket)}): {basket}") # Duplicates are automatically removed

# FROZENSET: Same as set, but immutable.
locked_basket = frozenset(basket)
print(f"Frozenset ({type(locked_basket)}): {locked_basket}")

# --- 6. BOOLEAN TYPE (bool) ---
print("\n--- 6. BOOLEAN TYPE ---")

# BOOL: Represents one of two values: True or False. Used for logical operations.
is_valid = (18 > 16)
is_logged_in = True

print(f"Is 18 > 16? {is_valid} ({type(is_valid)})")
print(f"Is Logged In: {is_logged_in} ({type(is_logged_in)})")