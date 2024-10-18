"""
Author:Davis Christy Robert
Date:18-10-2024
Description:a Python program that demonstrates the usage of arithmetic,
comparison, and logical operators.
Perform a few operations and print the results.
Expected Output:

Sum: 15, Division: 2.0

Is a greater than b?: True

Are a and b equal?: False

Logical AND: True

Logical OR: True
"""
a=int(input("enter your number"))
b=int(input("enter your number"))
print("sum:",a+b,"Division:",a/b)
print("Is a greater than b",a>b,)
print("Are a and b equal?:",a==b)
print("Logical AND:",a==10 and b==5)
print("Logical OR:",a>b or a<b)