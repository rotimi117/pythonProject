# convert_cel_to_far() which takes one float parameter representing
# degrees Celsius and returns a float representing the same temper-
# ature in degrees Fahrenheit using the following formula:
# F = C * 9/5 + 32
# Enter a temperature in degrees
# 72 degrees F = 22.22 degrees C

Celsius = int(input("Enter a temperature in degrees F:  "))
Fahrenheit = Celsius * 9/5 + 32
print(f"{Celsius} degrees F = {Fahrenheit:,.2f} degrees C")