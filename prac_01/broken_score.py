"""
CP1404/CP5632 - Practical
Broken program to determine score status

Pseudocode:

get score

if score < 0 or score > 100:
    then display invalid score message
else if score >= 90:
    then display excellent message
else if score >= 50:
    then display passable message
else:
    then display bad message

"""


# Solution

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
