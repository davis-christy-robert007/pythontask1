"""
Author:Davis Christy Robert
Description:Program to find the factorial of a number using Recursion.
date:29-11-2024

"""
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the number"))
print("the factorial of ",n, "is",factorial(n))