def find_minimum(array):
    minimum = array[0]

    for num in array:
        if num < minimum:
            minimum = num

    return minimum

numbers = [10, 5, 8, 15, 3, 20]
minimum_number = find_minimum(numbers)
print("The smallest number is:", minimum_number)
