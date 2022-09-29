"""
Program that converts between Celsius and Fahrenheit temperatures.
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def calculate_fahrenheit():
    return celsius * 9.0 / 5 + 32


def calculate_celsius():
    return 5 / 9 * (fahrenheit - 32)


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = calculate_fahrenheit()
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit:"))
        celsius = calculate_celsius()
        print(f"Result: {celsius:2f}C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
