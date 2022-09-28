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

password = input("Enter password:")

if len(password) < 7:
    while len(password) < 7:
        print("Password too short. Try again.")
        password = input("Enter password:")

for character in password:
    print('*', end='')
