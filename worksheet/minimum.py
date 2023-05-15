number1 = int(input('enter a number: '))
number2 = int(input('enter second number: '))
number3 = int(input('enter third number: '))
minimum = number1
if number1 > minimum:
     minimum = number2
     if number3 < minimum:
         minimum = number3
         print('minimun value is ', minimum)
