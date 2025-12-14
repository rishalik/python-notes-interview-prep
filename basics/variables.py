"""A variable in Python is essentially a named location in the computer's memory that stores a value. Think of it as a labeled box where you put different kinds of data.

In Python, unlike some other programming languages, you do not need to explicitly declare the variable type (like integer, string, etc.) before using it. Python is a dynamically typed language, meaning the type of the variable is determined at runtime based on the value you assign to it."""

"""1. Creating (Declaring) and Assigning Variables
The process of creating a variable and giving it a value is called assignment, and it is done using the single equals sign (=)."""

# Example 1: Basic Assignment
# Create an integer variable
age = 30

# Create a string variable
name = "Alice"

# Create a floating-point variable
pi_value = 3.14159

# Create a boolean variable
is_student = True

# Print the values and types
print(age)         # Output: 30
print(name)        # Output: Alice
print(type(age))   # Output: <class 'int'>
print(type(name))  # Output: <class 'str'>

"""2. Variable Naming Rules
There are a few simple but important rules you must follow when naming your variables:

Must start with a letter (a-z, A-Z) or an underscore (_).

Cannot start with a number.

Can only contain alphanumeric characters (A-z, 0-9) and underscores (_).

Case-sensitive: myVariable is different from myvariable.

Cannot be one of Python's reserved keywords (e.g., for, if, while, True, False, class).
"""
# Example 2: Valid and Invalid Names

# Valid variable names
user_age = 25
_temporary_value = 100
MaximumValue = 500

# Invalid variable names (would cause an error if executed)
# 2nd_data = "Error"
# user-name = "Error"
# while = 7  # 'while' is a reserved keyword

"""3. Conventions for Variable Naming
While not mandatory, Python programmers typically follow these conventions (known as snake_case):

Use all lowercase letters.

Separate words with underscores."""

# Example: user_input, total_price, start_time

"""4. Reassigning and Dynamic Typing
A key concept is that a variable's value can be changed, and even its type can be changed, after it is created.
"""
# Example 3: Reassignment

x = 10         # x is an integer (int)
print(x)       # Output: 10

x = 20.5       # Reassign x with a new float value (x is now a float)
print(x)       # Output: 20.5

x = "Hello"    # Reassign x with a new string value (x is now a string)
print(x)       # Output: Hello

"""5. Assigning Multiple Variables
Python allows you to assign a single value to multiple variables simultaneously, or assign different values to multiple variables in a single line.
"""

# Example 4: Multi-Assignment

# Assign the same value to three variables
a = b = c = 5
print(a, b, c)  # Output: 5 5 5

# Assign different values to three variables (Tuple Unpacking)
x, y, z = "Red", 10, False
print(x)  # Output: Red
print(y)  # Output: 10
print(z)  # Output: False

"""6. Variable Scope (Briefly)
Variables exist within a certain scope. For instance, a variable created outside of any function has a global scope and can be used anywhere in the program. A variable created inside a function has a local scope and only exists while that function is running.
"""
global_var = "I am everywhere"  # Global variable

def my_function():
    local_var = "I am only in the function"  # Local variable
    print(global_var)

my_function()
# print(local_var) # This would cause an error because local_var is out of scope

print(global_var)

# In summary: Python variables are flexible, dynamically typed containers for data. You create them instantly with an assignment (=), and they must follow simple naming rules.