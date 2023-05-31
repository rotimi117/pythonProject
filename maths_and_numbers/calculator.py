def addition(a,b):
    return (a + b)

def subraction(a,b):
    return (a - b)

def multiplication (a,b):
    return (a * b)

def division (a,b):
    return (a // b)

def digital_calculator(a:int, b: int, operator:str ):
    if operator == "+":
        return addition (a, b)
    if operator == "-":
        return subraction(a,b)
    if operator == "*":
        return multiplication (a, b)
    if operator == "//":
        return division(a,b)

a = int(input("Enter a number: "))
b = int(input("Enter a number:  "))
operator = input("Enter an operator: ")
print(digital_calculator(a,b,operator))



