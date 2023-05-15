total = 0
smallest = float('inf')
largest = float('-inf')

for day in range(1, 8):
    infections = int(input(f"Enter the number of infections for day {day}: "))


    total += infections

    if infections < smallest:
        smallest = infections
    if infections > largest:
        largest = infections

average = total / 7

print(f"\nTotal infections: {total}")
print(f"Average infections per day: {average}")
print(f"Smallest daily infections: {smallest}")
print(f"Largest daily infections: {largest}")

