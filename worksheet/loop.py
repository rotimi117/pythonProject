investment = int(input('Enter amount you want to invest:   '))
years = int(input('Enter how long you want to invest:  '))
interest = 0.05
for years in range(1,years+1):
    return_on_invest = investment * interest
    future_value = investment + return_on_invest
    investment = future_value
    print(f"year{years} return on investment {return_on_invest}, your investment is now {future_value}")

    def investment(investment, years):
        interest = 0.05
        for years in range(1, years + 1):
            return_on_invest = investment * interest
            future_value = investment + return_on_invest
            investment = future_value
            print(f"year{years} return on investment {return_on_invest}, your investment is now {future_value}")

def multiplication(i, j):
    for i in range(1, 13):
        for j in range(1, 13):
            print(f"{i} x {j} = {i * j}")
        print()
first_user_input = (int(input("Enter your first value: ")))
second_user_input = (int(input("Enter your second value: ")))
print(multiplication(first_user_input, second_user_input))


investment = int(input('Enter amount you want to invest:   '))
years = int(input('Enter how long you want to invest:  '))
interest = 0.05
count = 1
while count <= years:
    return_on_invest = investment * interest
    future_value = investment + return_on_invest
    investment = future_value
    count+=1
    print(f"year{years} return on investment {return_on_invest}, your investment is now {future_value}")


numbers = 2
for num in range(10):
    print(numbers)

interger = 2
while interger < 11:
    print(interger)
    interger = interger + 1


def double(number):
    return number * 2

numbers = int(input("Enter a number:  "))
for num in range(3):
    numbers = double(numbers)
    print(numbers)

number = int(input("Enter a number lad:  "))
for num in range(3):
   number = number * 2
   print(number)