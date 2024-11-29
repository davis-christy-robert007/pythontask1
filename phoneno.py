"""
Author:Davis Christy Robert
description:program to check whether the given number is a valid mobile number or not using functions.

Rules:

    Every number should contain exactly 10 digits.
    The first digit should be 7 or 8 or 9
date:29-11-2024
"""

def phonenumb():
    n=input("enter the number to be checked:")
    if len(n)==10 and n[0] in '7,8,9':
        print("number is valid")
    else:
        print("the number is not valid")
phonenumb()