"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the user enters a number that is not an integer, such as a string,
float, or whitespace.

2. When will a ZeroDivisionError occur?
When the user enters 0 as the denominator, which is mathematically
impossible.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
You could write an if statement that activates a while validation loop if a
user enters a zero then displays an invalid number message, to prevent the
user from entering the number 0.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        while denominator == 0:
            print("You can't divide by zero! That's mathematically impossible!")
            denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
