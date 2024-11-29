"""
Author:Davis Christy Robert
Description:Recursive function to add two positive numbers.
date:29-11-2024
"""
def add(num1,num2):
    if num2==0:
        return num1
    else:
        return  add(num1+1,num2-1)
num1=int(input("enter the first  number"))
num2=int(input("enter the second number"))
print("sum of two numbers",num1 ,"and",num2," is:",add(num1,num2))