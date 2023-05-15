list is mutable
my_list = []
name = ["sultan", "mariam", "torin", "awal", "david"]
student = [["sultan",35, 400, 90.5],["mariam", 32,300,95.0]]
print(student[0][0])
ones = [1] * 100

list2 = student + name
print(name[::-1])

even_number = []
for n in range(0,51,2):
    even_number.append(n)
    print(even_number)

even_number = list(range(0,51,2))
print(even_number)


numbers = [1,2,3,4,5]
x = 1
y = 5
x, y , *others, = numbers
print(x,others,y)

letters = list("hello c16")
print(letters)

for index,letters in enumerate(letters):
    print(index,letters)

letters = list('abcd')
letters.append('e')
letters.append('f')
letters.remove("c")
del letters[0:2]
letters.insert(0, 't')
print(letters)


my_list = 0
cart = [['rotimi',1000, 20 , 20_000, '23465674372']],[['dele',2000,30,60000,'090776854654']],[['haaland',5000,50,250000,'09775656545453']],[['saka',6000,60,360000,'90886848490']],[['jesus',4000,40,120000,'09765637378228']]
cart[0][1] = 7000
cart[0][1] = 'benny blanco'

number = list(range(1,21))
print(number)
odd_number = []
for n in number:
    if n % 2 != 0:
        odd_number.append(n)
print(odd_number)

number[4:10] = [0] * 5
print(number)

number[5:10] = [0] * len(number[5:10])
print(number)

first_seven = number[:7]
print(first_seven)

number[:] = []
print(number)


list1 = [4,1,1,1,2,2,3,1]
print(len(set(list1)))








