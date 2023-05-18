""" Accept input from user check if input is less than 0 (negative)
return error (invalid entry) else convert input to inches
"""

input = float(input())

if input < 0:
    print("Invalid Entry")
else:
    print(input/2.54)

