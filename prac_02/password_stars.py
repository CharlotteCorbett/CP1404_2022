"""
Pseudocode:
Get user password

If user password length < 7:
    While user password length < 7:
        Display invalid password message
        Get user password

For character in user password length:
    Display '*'
"""


def main():
    password = get_valid_password()
    print_password(password)


def print_password(password):
    for character in password:
        print('*', end='')


def get_valid_password():
    password = input("Enter password:")
    if len(password) < 7:
        while len(password) < 7:
            print("Password too short. Try again.")
            password = input("Enter password:")
    return password


main()
