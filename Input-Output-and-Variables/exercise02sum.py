"""
Exercise: 02 - Sum
Topic: Input, Output and Variables
Description:
    Prints the sum of two determined valid numbers.
"""

def ValidateInput(InputNumber):
    """
    Validates if the input is a rational number

    Args:
        InputNumber(float): User input
    
    Return:
        bool: True if it's a valid number, False otherwise
    """
    
    try:
        InputNumber = float(InputNumber)
    except ValueError:
        # Handles non-numeric numbers to prevent the program crash
        return False
    return True

# Repeats until the user provides a valid number
while True:
    firstnumber = input("\nPlease, enter the first number of the sum:\n")
    if ValidateInput(firstnumber):
        firstnumber = float(firstnumber)
        break
    print("\nInvalid number, please try again.")

while True:
    secondnumber = input("\nPlease, enter the second number of the sum:\n")
    if ValidateInput(secondnumber):
        secondnumber = float(secondnumber)
        break
    print("\nInvalid number, please try again.")

print(firstnumber + secondnumber)