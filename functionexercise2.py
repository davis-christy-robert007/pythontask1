"""
Author:Davis Christy Robert
Description:Python function to sum all the numbers in a list.
date:30-11-2024
"""
def sumofnum(numbers):
    total=0
    for i in numbers:
        total+=i
    print(total)
numbers=[]
n=int(input("enter the numberof elements:"))
for i in range(n):
    n1=int(input("enter a number"))
    numbers.append(n1)
print(sumofnum(numbers))


