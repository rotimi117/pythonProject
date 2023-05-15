# convert_far_to_cel() which take one float parameter representing
# degrees Fahrenheit and returns a float representing the same tem-
# perature in degrees Celsius using the following formula:
# C = (F - 32) * 5/9

# Enter a temperature in degrees C:
# 37 degrees C = 98.60 degrees F


Fahrenheit = int(input("Enter a temperature in degrees C: "))
Celsius = float(Fahrenheit - 32) * 5/9
print(f"{Fahrenheit} degrees C = {Celsius:,.2f} degrees F")
