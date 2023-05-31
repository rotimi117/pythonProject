# tuple is unmutable
# first in first out == queue
# last in first out == stack

# letters = ("a", "b", "c")
# numbers = (1,)
# list1 = [1, "1", "a", 2]
# print(list1)
# alpha_num = letters + numbers
# print(alpha_num)
# print(alpha_num[1:3])
#
# print(numbers)
# print(letters)
# print(type(letters))
# print(type(numbers))


# create of tuple of 1 to 500

# number = tuple(range(1,500))
# print(number)
# even_number =()
# for num in number:
#     if num % 2 == 0:
#         print(num)
#
# odd_number =()
# for num in number:
#     if num % 2 != 0:
#      print(num)

# num = tuple(range(1,501))
# print(num)
#
# num_odd = tuple(range(1,501,2))
# print(num_odd)
#
# num_even = tuple(range(2,501,2))
# print(num_even)
#
# number = num_odd + num_even
# print(number)
#
# x, y, z, *others = number
# print(x,y,z, others)


# cardinal_numbers = ("first","second","third")
# print(cardinal_numbers)
# print(cardinal_numbers[1])
# cardinal_numbers = ("position1","position2","position3")
# print(cardinal_numbers)
#
#
#
my_name = tuple("rotimi")
if "x" in my_name:
    print("The character 'x' is present in my_name.")
else:
    print("The character 'x' is not present in my_name.")
print(my_name)
name = tuple(my_name[1:])
print(name)


# food = ["rice","beans"]
# food.append("broccoli")
# food.extend(["bread","pizza"])
# print(food[:2])
# print(food[-1])




