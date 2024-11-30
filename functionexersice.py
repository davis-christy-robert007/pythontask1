"""
Author:Davis Christy Robert
Description:Python function to find the maximum of three numbers.
date:30-11-2024
"""
def maxnum():
    if x>y and x>z:
        print(x,"is the maximum")
    elif y>x and y>z:
        print(y,"is the maximum")
    elif z>x and z>y:
        print(z,"is the maximum")
x = int(input("enter the first nunmber:"))
y = int(input("enter the second number:"))
z = int(input("enter the third number:"))
maxnum()