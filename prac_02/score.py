"""
Program to determine score status

Initial Pseudocode:

get score

if score < 0 or score > 100:
    then display invalid score message
else if score >= 90:
    then display excellent message
else if score >= 50:
    then display passable message
else:
    then display bad message

Code taken from broken_score.py in prac_01, and refactored into functions
in this program.
"""

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")