# square = {}
# for i in range(1,11):
#     square[i] = i ** 2
# print(square)

square = (i ** 2 for i in range(1,11))
print(type(square))
