"""
CP1404/CP5632 - Practical
Let’s write a program that gets an integer from the user and does not crash when a non-number is entered.
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter an integer:"))  # TODO: this line
        break   # TODO: this line
        pass
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)