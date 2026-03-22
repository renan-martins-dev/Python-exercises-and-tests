"""
Exercise: 04 - Legal Age
Topic: Input, Output and Variables
Description:
    Checks if the given age is of legal age and prints the result.
"""

from datetime import datetime

LEGAL_AGE = 18

def ValidateInput(ProvidedYearOfBirth):
    """
    Validates if the input is a integer number

    Args:
        ProvidedYearOfBirth(int): User input
    
    Return:
        bool: True if it's a valid integer number, False otherwise
    """
    
    try:
        ProvidedYearOfBirth = int(ProvidedYearOfBirth)
    except ValueError:
        # Handles non-integers numbers to prevent the program crash
        return False
    return True

# Repeats until the user provides a valid integer number
while True:
    UserYearOfBirth = input("\nPlease, enter the year of birth to be checked:\n")
    if ValidateInput(UserYearOfBirth):
        UserYearOfBirth = int(UserYearOfBirth)
        UserAge = datetime.now().year - UserYearOfBirth
        if UserAge == LEGAL_AGE:
            # Checks if the user already had their birthday this year
            while True:
                UserMonthOfBirth = input("\nPlease, enter the month of birth in number to be checked:\n")
                if ValidateInput(UserMonthOfBirth):
                    UserMonthOfBirth = int(UserMonthOfBirth)
                    # Determines the actually user age else asks for the day birth to confirm the age
                    if datetime.now().month < UserMonthOfBirth:
                        UserAge = UserAge-1
                    elif datetime.now().month == UserMonthOfBirth:
                        while True:
                            UserDayOfBirth = input("\nPlease, enter the day of birth in number to be checked:\n")
                            if ValidateInput(UserDayOfBirth):
                                UserDayOfBirth = int(UserDayOfBirth)
                                if datetime.now().day < UserDayOfBirth:
                                    UserAge = UserAge-1
                                break
                            print("\nInvalid number, please try again.")
                    break
                print("\nInvalid number, please try again.")
        break
    print("\nInvalid number, please try again.")

# Identifies if the user is of legal age
if UserAge >= LEGAL_AGE:
    print(f"User is of legal age")
else:
    print(f"User is not of legal age")