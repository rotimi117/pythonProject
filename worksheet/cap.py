text = 'my name is rotimi'
print(text)

string = " my name is rotimi nicol"
print(string)

string = "that is rotimi's book"
print(string)

string = "my name is oluwadurotimi obabiyi-nicol\i am 22 years old\i attended babcock university\i studied computer science"
print(string)

string = ("""my name is oluwadurotimi obabiyi-nicol 
i am 22 years old 
i attended babcock university 
i studied computer science""")
print(string)

name = 'rotimi nicol'
print(len(name))

name = 'rotimi nicol'
print(name[2:8])

name = "bazinga"
print(name[2:6])

name = "Animal,Badger,Honey Bee,Honeybadger"
print(name.lower())

name = "Animal,Badger,Honey Bee,Honeybadger"
print(name.upper())

string1 = "     Filet Mignon"
print(string1.lstrip())

string2 = "Brisket    "
print(string2.rstrip())

string3 = "    Cheeseburger    "
print(string3.strip())

string1 = "become"
print(string1.startswith('be'))

string2 = "Becomes"
print(string2.startswith('Be'))

string3 = 'BEAR'
print(string3.startswith('BE'))

string4 = 'bEautiful'
print(string4.startswith('bE'))


#user = input("what are you doing ")
#print('im coding' , user)

#user = input('what are you doing ')
#output = user.lower()
#print('im coding', output)

#user = input('enter your name ')
#output = user[1:7]
#print(output)

#user = input('enter your password: ')
#output = user[0:2].upper()
#print('The first letter you entered was: ', output)

#user = input('what is your name: ')
#output = len(user)
#print(output)


number = '35'
output = int(number)
print(output * 2)

number = "70.0"
output = float(number)
print(output * 2)

name = 'i am' + str(10) + 'years old'
print(name)

user1 = input('enter a number: ')
user2 = input('enter a number: ')
output = float(int(user1) * int(user2))
print("the product of 20 and 2 is " ,output)

weight = 0.2
animal = 'newt'
output = (str(weight) + 'kg' + 'is' + 'weight' + 'of' + 'the' + animal)
print(output)

weight = 0.2
animal = 'newt'
output = "{} kg is weight of the {}".format(weight,animal)
print(output)

weight = 0.2
animal = 'newt'
output = f"{weight} kg is weight of the {animal}"
print(output)

name = "the surprise is in here somewhere"
output = name.find("here")
print(output)

text = 'AAA'
output = text.find('a')
print(output)

text = "Somebody said something to Samantha."
output = text.replace("s","x")
print(output)

#text = input("Somebody said something to Samantha:  ")
#output = text.find("bloody")
#print(output)

num1 = 25_000_000
num2 = 25000000
print(num1)
print(num2)

num = 175000.0
output = 175e3
print(output)

num =2e320
print(num)

base = input("enter a number:  ")
exponent = input("enter a number: ")
output = int(base) ** int(exponent)
print(base, 'to the power of', exponent,'is', output)

num = 0.1 + 0.2
print(num)

user = input("Enter a number: ")
output = float(user)
output = round(output,2)
print(user,'rounded to 2 decimal places is',output)

user = input('Enter a number:  ')
output = float(user)
output = abs(output)

user1 = input('Enter a number:   ')
user2 = input('Enter a number:   ')
process = float(user1), float(user2)
output = num.is_integer()
print('The difference between',user1,'and',user2,'is an integer?',output)

num = 3 ** .125
print(f"{num:.3f}")

num = 150000
print(f"{num:,.2f}")

num = 2 / 10
print(f"{output:.0%}")

def cube(num):
    output = num ** 3
    return output

print(f"4 cubed is {cube(4)}")
print(f"7 cubed is {cube(7)}")

def greet(name):
    return o
print(f"hello {greet(name)}")

greet("rotimi")























