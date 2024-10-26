"""
Author: Davis Christy robert
Date: 25-10-2024
Description: Python program to Familiarize time and date in various formats
"""
from datetime import datetime

current=datetime.now()
print(current)

Format_1=(current.strftime("%Y-%m-%d-%H-%M-%S"))
print(Format_1)


Format_2=(current.strftime("%m/%d/%Y"))
print(Format_2)

Format_3=(current.strftime("%A,%B %d,%Y"))
print(Format_3)

Format_4=(current.strftime("%A,%B %d,%Y %H:%M:%S %p"))
print(Format_4)

Format_5=(current.strftime("%a-%b-%d %H:%M:%S IST %Y"))
print(Format_5)

Format_6=(current.strftime("%a-%b-%d %H:%M:%S IST %Y"))
print(Format_6)

Format_7=(current.isoformat())
print(Format_7)


Date=(current.strftime("%d"))
print(Date)

Time=(current.strftime("%H:%M:%S"))
print(Time)

Month=(current.strftime("%B"))
print(Month)

Year=(current.strftime("%Y"))
print(Year)
