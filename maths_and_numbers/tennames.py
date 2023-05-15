# name_list = []
# count = 1
# while (count <= 5):
#
#     name = input("Enter a name: ")
#
#     if len(name) > 0 and len(name) <=10:
#         name_list.append(name)
# print("Names collected:", name_list)

name_list = []

while len(name_list) < 10:
    name = input('Enter a name:  ')
    if len(name)<10:
        break

    name_list.append(name)

print(name_list)