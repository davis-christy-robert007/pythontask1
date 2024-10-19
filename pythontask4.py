"""
Author:davis christy robert
date:18-10-20
description:Python program that uses functions from the math module to perform the following operations on a number provided by the user:
Square root of 5: 2.23606797749979

Factorial of 5: 120

5 raised to power 2: 25.0
"""
import math
number=int(input("enter the number"))
print("Square root of",number,":",math.sqrt(number))
print("Factorial of ",number,":",math.factorial(number))
print(number," raised to power 2:",math.pow(number,2))
