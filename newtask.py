"""Author:Davis Christy Robert
Date:25-10-2024
description:Write a Python program to find the largest of two numbers.
The program should take two numbers as input from the user and determine which one is the largest.
Use conditional statements to compare the numbers.
"""
number1=int(input("enter the number:"))
number2=int(input("enter the number:"))
if number1>number2:
    print(number1,"is greater than",number2)
else:
    print(number2, "is greater than ",number1)
