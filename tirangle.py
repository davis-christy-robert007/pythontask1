"""
Author:Davis Christy Robert
 Description:A program that accepts the lengths of three sides of a triangle as inputs.
The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle,
 the square of one side equals the sum of the squares of the other two sides). Implement using functions.

Example Runs:

Example 1

    Enter the length of the first side: 3
    Enter the length of the second side: 4
    Enter the length of the third side: 5
    The given triangle is a right triangle.

Example 2:

    Enter the length of the first side: 2
    Enter the length of the second side: 3
    Enter the length of the third side: 4
    The given triangle is not a right triangle.
date:29-11-2024

"""


def check_right_triangle(sides):
    sides.sort()
    if sides[2]**2 == sides[0]**2 + sides[1]**2:
        return True
    return False
sides=[]
sides.append(int(input("enter the length of the first side:")))
sides.append(int(input("enter the length of the second side:")))
sides.append(int(input("enter the length of the third side:")))
if check_right_triangle(sides):
    print("The given triangle is a right triangle")
else:
    print("The given triangle is not a right triangle")