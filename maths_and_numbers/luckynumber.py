
# for num in range(1,11):
#     lucky_number = int(input("Enter your lucky number:   "))
#     if num >= 51:
#         print("number not a lucky number ")
#     else:
#         print("number is a lucky number ")

number = 50

lucky_number = int(input("Enter your lucky number:  "))
while lucky_number != number:
    lucky_number = int(input("Try again LAD!!"))

print("congratulation LAD lucky number is ",lucky_number)