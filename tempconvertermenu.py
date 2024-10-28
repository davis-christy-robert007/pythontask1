"""Author:Davis Christy Robert
Date:28-10-2024
description:Write a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit.
 The program should repeatedly display a menu with three options:

    Convert Celsius to Fahrenheit
    Convert Fahrenheit to Celsius
    Exit the program
"""


while True:
    print("1.\tConvert Celsius to Fahrenheit")
    print("2.\tConvert Fahrenheit to Celsius")
    print("3.\tExit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        temperature_convert = int(input("enter the temperature:"))
        fahrenheit=temperature_convert * 9 / 5 + 32
        print(f"celsius to fahrenheit is ",fahrenheit)
    elif choice==2:
        temperature_convert = int(input("enter the temperature:"))
        celsius = (temperature_convert - 32 * 5 / 9)
        print("fahrenheit to celsius is",celsius)
    elif choice==3:
        break