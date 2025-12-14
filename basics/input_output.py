# ===============================================
# PYTHON FUNDAMENTALS: INPUT AND OUTPUT (I/O)
# ===============================================

# I/O refers to how a program gets data (Input) and sends data (Output).

# --- 1. OUTPUT: THE print() FUNCTION ---
# The primary way to display data to the console.

print("\n--- 1. OUTPUT: The print() Function ---")

# 1.1 Basic Print
print("Hello, Python!")

# 1.2 Printing Variables
name = "Alex"
score = 98.5
print("The player", name, "scored", score, "points.")

# 1.3 Customizing Separator (sep)
# The 'sep' argument changes the default space between printed items.
print("A", "B", "C", sep="---") # Output: A---B---C

# 1.4 Customizing End (end)
# The 'end' argument changes the default newline character (\n).
print("Starting here...", end=" ")
print("...and ending here (on the same line).")
print("\n") # Print an empty line for separation

# 1.5 Formatted Output (f-Strings)
# f-strings (Formatted String Literals) are the modern, easy way to format output.
width = 10
height = 5
area = width * height

print(f"The rectangle is {width} wide and {height} tall.")
print(f"Calculated area is: {area}")


# --- 2. INPUT: THE input() FUNCTION ---
# Used to accept data from the user via the console.
# IMPORTANT: The input() function ALWAYS returns the user's input as a string (str).

print("\n--- 2. INPUT: The input() Function ---")

# 2.1 Basic String Input
# The text inside the parentheses is the prompt shown to the user.
city = input("Please enter your city name: ")
print(f"You entered the city: {city}")
print(f"The type of 'city' is: {type(city)}") # Notice it's always 'str'

# 2.2 Handling Numerical Input (Type Conversion)
# Input must be explicitly converted (type casting) to perform math.

user_age_str = input("Enter your age: ")
print(f"Input type before conversion: {type(user_age_str)}") 

# Convert the string input to an integer (int)
try:
    user_age_int = int(user_age_str)
    
    # Now we can perform math
    age_next_year = user_age_int + 1
    
    print(f"Next year, you will be {age_next_year} years old.")
    print(f"Input type after conversion: {type(user_age_int)}") 

except ValueError:
    # This block handles cases where the user enters non-numeric text
    print("Error: That wasn't a valid number for age.")


# --- 3. COMBINING I/O: INTERACTIVE PROGRAM ---
print("\n--- 3. COMBINING I/O: Interactive Calculation ---")

# Get two numbers
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Convert to float to handle decimals
try:
    num1 = float(num1_str)
    num2 = float(num2_str)
    
    # Calculate and output the result
    total_sum = num1 + num2
    
    print(f"\nResult: The sum of {num1} and {num2} is: {total_sum}")
    
except ValueError:
    print("\nInvalid input! Please restart and enter only numbers.")