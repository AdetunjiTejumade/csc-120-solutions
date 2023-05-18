"""
Accept temp value
if temp less than -273.15 print invalid
elif it is exactly -273.15 print temp is absolute 0
elif it is between -273.15 and 0 print temp is below freezing
elif value is 0 print temp is at the freezing point
elif value is between 100 and 0 print temperature is in the normal range.
elif value is 100 print temperature is at the boiling point.
elif value is above 100 print temperature is above the boiling point.
else(i.e all previous conditions fail) print Invalid Entry
"""

value = float(input())

if value < -273.15:
    print("invalid")
elif value == -273.15:
    print("Temp is absolute zero")
elif value > -273.15 and value < 0:
    print("temp is below freezing")
elif value == 0:
    print("Temp is at the freezing point")
elif value > 0 and value < 100:
    print("temperature is in the normal range.")
elif value == 100:
    print("temperature is at the boiling point.")
elif value > 100:
    print("temperature is above the boiling point.")
else:
    print("Invalid Entry")
