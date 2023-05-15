square = [[0 for j in range(4)] for i in range(4)]

square[2][2] = 16

print(" ", end="\t")
for j in range(4):
    print(j, end="\t")
print()
for i in range(4):
    print(i, end="\t")
    for j in range(4):
        print(square[i][j], end="\t")
    print()
