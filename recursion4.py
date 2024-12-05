"""
Author:Davis Christy Robert
Description:Recursive function to find the greatest common divisor of two positive numbers.
date:29-11-2024
"""
def gcd(num1,num2):
    if num1 % num2 == 0:
        return num2
    else:
       return gcd(num2,num1%num2)
num1=int(input("enter the first  number:"))
num2=int(input("enter the second number:"))

print(gcd(num1,num2))