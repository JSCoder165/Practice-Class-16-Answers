# done without max() intentionally

import random
def largest(num1, num2, num3):
    if(num1>num2 and num1>num3):
        return num1
    elif (num2>num1 and num2>num3):
        return num2
    elif (num3 > num2 and num3>num1):
        return num3
    else:
        return num1
"""
num1 = input("Enter the first num: ")
num2 = input("Enter the second num: ")
num3 = input("Enter the third num: ")
"""

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)
print(f"largest num is: {largest(num1, num2, num3)}")
print(num1, num2, num3)
