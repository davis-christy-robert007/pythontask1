"""
Author:Davis Christy Robert
Date:25-10-2024
description:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit.
 The user should be able to input a temperature in Celsius or Fahrenheit,
  and the program should convert it to the other unit using the formula:

"""
temperature=int(input("enter the temperature:"))
cor=input("Is this in (C)elsius or (F)ahrenheit?:")
if cor =="C" or cor=="c":
    Fahrenheit=(9/5*temperature)+32
    print(temperature,"Celsius is ",Fahrenheit,"Fahrenheit")
elif cor=="F" or cor=="f":
    celsius=(5/9*(temperature-32))
    print(temperature,"Fahrenheit is ",celsius,"celsius")
else:
    print("wrong temperature code.")








