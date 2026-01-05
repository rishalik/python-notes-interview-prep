# ===============================================
# PYTHON INTERMEDIATE: POLYMORPHISM
# ===============================================

# Polymorphism allows different objects to respond to the 
# same method call in their own specific way. It simplifies 
# code by letting us treat different types through a common interface.

# [VISUAL REPRESENTATION]
# Method Call: .speak()
#      /          |          \
# [Dog Obj]   [Cat Obj]   [Duck Obj]
#  "Woof!"     "Meow!"     "Quack!"



class WhatsApp:
    def send_message(self):
        print("Sending WhatsApp message: ")

class Email:
    def send_message(self):
        print("Sending Email: ")

class SMS:
    def send_message(self):
        print("Sending SMS: ")

# 1. Polymorphism with Functions
def notify_user(notification_type):
    """
    This function doesn't care if it's an Email, SMS, or WhatsApp object.
    As long as the object has a 'send_message' method, it will work.
    """
    notification_type.send_message()

def main():
    print("--- 1. POLYMORPHISM VIA COMMON INTERFACE ---")
    # Objects of different classes
    app_msg = WhatsApp()
    mail_msg = Email()
    text_msg = SMS()

    # We can pass any of them to the same function
    notify_user(app_msg)
    notify_user(mail_msg)
    notify_user(text_msg)

    print("\n--- 2. POLYMORPHISM VIA ITERATION ---")
    # We can store them in a list and treat them identically
    services = [WhatsApp(), Email(), SMS()]

    for service in services:
        service.send_message()

    print("\n--- 3. BUILT-IN POLYMORPHISM ---")
    # The len() function is polymorphic; it works on different types
    print(f"Length of string 'Python': {len('Python')}")
    print(f"Length of list [1, 2, 3]: {len([1, 2, 3])}")

if __name__ == "__main__":
    main()