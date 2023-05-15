my_list = list(range(1,21))
print(my_list)

third_number = my_list[3]
print(third_number)

first_five = my_list[:5]
print(first_five)

first_half = my_list[:10]
print(first_half)

last_five = my_list[15:20]
print(last_five)

my_list[:] = []
print(my_list)

my_list = list(reversed(my_list))
print(my_list)

third_last = my_list[17]
print(third_last)

numbers = list(range(1, 21))


third_number = numbers[2]
first_five_numbers = numbers[:5]
first_half = numbers[:len(numbers)//2]
last_five_numbers = numbers[-5:]
every_other_number = numbers[::2]
numbers_in_reverse = numbers[::-1]
third_last_number = numbers[-3]


print("Third number:", third_number)
print("First five numbers:", first_five_numbers)
print("First half of the list:", first_half)
print("Last five numbers:", last_five_numbers)
print("Every other number:", every_other_number)
print("Numbers in reverse order:", numbers_in_reverse)
print("Third last number:", third_last_number)


