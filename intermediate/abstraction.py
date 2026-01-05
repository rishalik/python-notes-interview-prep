# ===============================================
# PYTHON INTERMEDIATE: ABSTRACTION
# ===============================================

# Abstraction is used to hide the complex implementation 
# details and only show the necessary features. It enforces 
# a "contract" that child classes must follow.

# [CONCEPTUAL DIAGRAM]
#       +--------------------------+
#       |  ABSTRACT CLASS (Shape)  | <--- Cannot be instantiated
#       |  [Method: area()]        |
#       +------------+-------------+
#                    |
#        +-----------+-----------+
#        |                       |
# +------v-------+       +-------v-------+
# |    Circle    |       |    Square     | <--- Concrete Classes
# | (Impl. area) |       | (Impl. area)  |      (Must define area)
# +--------------+       +---------------+

from abc import ABC, abstractmethod



class PaymentProcessor(ABC):
    """
    Abstract Base Class (ABC). 
    This class acts as a template for all payment types.
    """

    @abstractmethod
    def validate_transaction(self, amount):
        """This must be implemented by any child class."""
        pass

    @abstractmethod
    def process_payment(self, amount):
        """This must be implemented by any child class."""
        pass

    def common_receipt(self, amount):
        """Abstract classes can also have normal methods."""
        print(f"Generating receipt for ₹{amount}...")

class UPIPayment(PaymentProcessor):
    def validate_transaction(self, amount):
        print(f"Validating UPI PIN for ₹{amount}...")
        return True

    def process_payment(self, amount):
        print(f"Processing UPI payment of ₹{amount} through NPCI server.")

class CardPayment(PaymentProcessor):
    def validate_transaction(self, amount):
        print(f"Checking CVV and OTP for ₹{amount}...")
        return True

    def process_payment(self, amount):
        print(f"Charging ₹{amount} to the Credit/Debit Card.")

def main():
    print("--- 1. ATTEMPTING TO INSTANTIATE ABSTRACT CLASS ---")
    try:
        # This will fail because PaymentProcessor is abstract
        generic_payment = PaymentProcessor()
    except TypeError as e:
        print(f"Error: {e}")

    print("\n--- 2. CONCRETE IMPLEMENTATION: UPI ---")
    upi = UPIPayment()
    if upi.validate_transaction(500):
        upi.process_payment(500)
        upi.common_receipt(500)

    print("\n--- 3. CONCRETE IMPLEMENTATION: CARD ---")
    card = CardPayment()
    if card.validate_transaction(1200):
        card.process_payment(1200)
        card.common_receipt(1200)

if __name__ == "__main__":
    main()