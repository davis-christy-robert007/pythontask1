"""
AUTHOR:DAVIS CHRISTY ROBERT
DATE:22-11-2024
DESCRIPTION:AIM: Input two lists from the user. Merge these lists into a third list such that in the merged list,
all even numbers occur first followed by odd numbers.
 Both the even numbers and odd numbers should be in sorted order.

"""
list1=[] #we are creating an empty list called list1
n=int(input("enter the value of n:")) #the value
for i in range(n):
    num=int(input("enter the num:"))
    list1.append(num)
print(list1)
list2=[]
n=int(input("enter the value of n:"))
for i in range (n):
    num=int(input("enter the num:"))
    list2.append(num)
print(list2)
list3=list1+list2
even_list=[]
odd_list=[]
for i in list3:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
merged_list=[]
merged_list=even_list+odd_list
print(merged_list)