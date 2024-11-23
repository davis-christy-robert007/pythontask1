""""
AUTHOR:DAVIS CHRISTY ROBERT
DATE:22-11-2024
DESCRIPTION:AIM: Input two lists from the user. Merge these lists into a third list such that in the merged list,
all even numbers occur first followed by odd numbers.
 Both the even numbers and odd numbers should be in sorted order.
"""
n=int(input("enter the value of n:"))
print("INCREASING TRIANGLE")
for i in range(n):
    for j in range(i,i+1):
        print("*"*j)

n=int(input("enter the value of n:"))
print("DECREASING TRIANGLE")
for i in range(n,0,-1):
    for j in range(i,i+1):
        print("*"*j)

num=int(input("enter the value of n:"))
print("HILL PATTERN")
for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end=" ")
    for j in range(i*2-1):
        print("*",end=" ")
    print()
num=int(input("enter the value of n:"))
print("REVERSE HILL PATTERN")
for i in range(num,0,-1):
    for j in range(num-i):
        print(" ",end=" ")
    for j in range(i*2-1):
        print("*",end=" ")
    print()
  
