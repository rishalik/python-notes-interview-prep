# ===============================================
# PYTHON FUNDAMENTALS: CONTROL FLOW
# ===============================================

# Control flow is the order in which code is executed. It uses 
# logic (if-else) and repetition (loops) to make programs dynamic.

def main():
    # 1. CONDITIONAL LOGIC
    # Decides which block of code runs based on a condition.
    # 
    temperature = 25

    if temperature > 30:
        print("It's a hot day.")
    elif temperature >= 20:
        print("It's a pleasant day.")
    else:
        print("It's a cold day.")

    # 2. FOR LOOPS
    # Used for iterating over a sequence (list, range, string).
    # 

    # [PROCESS FLOW]
    #       +--------------------------+
    #       |   Any items in list?     | <-------+
    #       +------------+-------------+         |
    #                    |                       |
    #            [Yes] --+-- [No]                |
    #              |          |                  |
    #      +-------v-------+  +------v-------+   |
    #      | Assign Item   |  |  Exit Loop   |   |
    #      +-------+-------+  +--------------+   |
    #              |                             |
    #      +-------v-------+                     |
    #      | Run Code Block| --------------------+
    #      +---------------+


    print("\nIterating through a list:")
    for color in ["Red", "Green", "Blue"]:
        print(f"Color: {color}")

    # 3. WHILE LOOPS
    # Runs as long as a condition remains True.
    count = 3
    print("\nCountdown:")
    while count > 0:
        print(count)
        count -= 1

    # 4. LOOP CONTROL
    # break: stops the loop | continue: skips to the next iteration.
    print("\nLoop Control Example:")
    for i in range(1, 6):
        if i == 3:
            continue  # Skip 3
        if i == 5:
            break     # Stop at 5
        print(f"Number: {i}")

if __name__ == "__main__":
    main()