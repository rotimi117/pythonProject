passes = 0
fails = 0

count = 1
while count <= 10:
    user = int(input('Enter a number:   '))
if user == 1 or user == 2:
    count +=1
    if user == 1:
        passes = passes + 1
fails = 10 - passes
print('passed',passes)
print('failed',fails)
if passes < 8:
    print('')