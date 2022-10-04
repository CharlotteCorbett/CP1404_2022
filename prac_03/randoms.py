"""
Answers:
What did you see on line 1?:
17, a whole number.
What was the smallest number you could have seen, what was the largest?:
Smallest: 5, Largest: 20

What did you see on line 2?:
7, a whole number, initial random number would have been the result of 5 + 2.

What was the smallest number you could have seen, what was the largest?:
Smallest: 5, Largest: 12

Could line 2 have produced a 4?:
No. The third parameter given in the .randrange function is +2.
2 + 3 = 5, != 4
To get a 4, the first parameter must be lowered to 2, for 2 + 2 = 4.

What did you see on line 3?:
4.791378888299535, a decimal (float) number with 15 decimal places behind the decimal point.

What was the smallest number you could have seen, what was the largest?:
Smallest: 2.5 * 10^-14, Largest: 5.5 * 10^-14

"""
import random

print(random.randint(0, 100))



