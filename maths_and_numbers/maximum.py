def find_maximum(array):
    maximum = array[0]

    for num in array:
        if num > maximum:
            maximum = num

    return maximum

numbers = [10, 5, 8, 15, 3, 20]
maximum_number = find_maximum(numbers)
print("The maximum number is:", maximum_number)
