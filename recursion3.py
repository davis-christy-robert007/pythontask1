"""
Author:Davis Christy Robert
Description: Recursive function to multiply two positive numbers
date:29-11-2024
"""
def multiply(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multiply(n1,n2-1)
n1=int(input("enter number 1:"))
n2=int(input("enter the number 2:"))
#multiply(n1,n2)
print("the product of two numbers ",n1,"and",n2,"is",multiply(n1,n2))
