# ===============================================
# PYTHON FUNDAMENTALS: FUNCTIONS, *ARGS & **KWARGS
# ===============================================

# Functions are reusable blocks of code. *args and **kwargs 
# allow functions to accept a flexible number of arguments.

# [FUNCTION ANATOMY]
#  def   greet_user  (name,  *args):
#   ^        ^          ^       ^
# Keyword   Name    Parameter  Extra Args

def profile_builder(required_name, *hobbies, **details):
    """
    *args (hobbies) collects extra positional arguments into a tuple.
    **kwargs (details) collects extra keyword arguments into a dictionary.
    """
    print(f"User: {required_name}")
    
    if hobbies:
        print(f"Hobbies: {hobbies}") # Tuple
        
    if details:
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")

def main():
    # Example 1: Simple function call
    print("--- Basic Call ---")
    profile_builder("Rishali")

    # Example 2: Using *args
    print("\n--- Call with *args ---")
    profile_builder("Alice", "Coding", "Hiking", "Photography")

    # Example 3: Using *args and **kwargs
    print("\n--- Call with *args and **kwargs ---")
    profile_builder("Bob", "Gaming", age=28, city="Bengaluru", role="Engineer")

if __name__ == "__main__":
    main()