"""
Author:Davis Christy Robert
Description:Program to define a module to find Fibonacci Numbers and import the module to another program.
Date:
"""



def fibonacci(n):
    a=0
    b=1
    
    
    for i in range(n-2):
        x=a+b
        print(x)
        a=b
        b=x


