# ===============================================
# PYTHON INTERMEDIATE: ENCAPSULATION
# ===============================================

# Encapsulation protects an object's internal state by 
# restricting direct access to variables. In Python, we 
# use underscores to signal 'Protected' or 'Private' data.

# [ACCESS MODIFIERS VISUAL]
# Name         Syntax      Access Level
# Public       name        Accessible from everywhere
# Protected    _name       Accessible within class & subclasses
# Private      __name      Accessible ONLY within the class



class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner            # Public: Can be accessed/changed freely
        self._account_type = "Savings" # Protected: Should only be used by subclasses
        self.__balance = balance      # Private: Cannot be accessed directly outside

    # Getter Method: To safely view private data
    def get_balance(self):
        return f"Current Balance: ₹{self.__balance}"

    # Setter Method: To safely modify private data
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn.")
        else:
            print("Insufficient funds or invalid amount!")

def main():
    account = BankAccount("Rishali", 5000)

    print("--- 1. ACCESSING PUBLIC DATA ---")
    print(f"Account Owner: {account.owner}")
    account.owner = "Rishali (Official)" # Works fine
    print(f"Updated Owner: {account.owner}\n")

    print("--- 2. ACCESSING PRIVATE DATA (The Error) ---")
    try:
        # This will trigger an AttributeError
        print(account.__balance)
    except AttributeError:
        print("Error: Cannot access '__balance' directly. It is private!\n")

    print("--- 3. USING GETTERS AND SETTERS ---")
    # This is the 'Encapsulated' way to interact with data
    print(account.get_balance())
    account.deposit(1500)
    print(account.get_balance())
    
    print("\n--- 4. MANGLED ACCESS (For Knowledge) ---")
    # Technically, Python 'mangles' the name to _BankAccount__balance
    # It's still reachable, but strongly discouraged.
    print(f"Sneaky access: {account._BankAccount__balance}")

if __name__ == "__main__":
    main()