""" Accept temp value
Accept unit
Convert based on unit provided
"""

value = float(input())
unit = str(input("Enter unit "))

if unit == "Celsius":
   print((value * 1.8) + 32)
elif unit == "Fahrenheit":
   print(((value - 32) / 1.8))



