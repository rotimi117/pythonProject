def unique_numbers(numbers):
    unique_nums = []
    sum_unique_nums = 0
    for num in numbers:
        if numbers.count(num) == 1:
            unique_nums.append(num)
            sum_unique_nums += num

    sum_all_nums = sum(numbers)
    difference = sum_all_nums - sum_unique_nums

    if difference % 2 == 0:
        return numbers
    else:
        return unique_nums


my_numbers = [1, 2, 3, 4, 2, 3, 5, 6, 6, 7, 8, 9, 9]
result = unique_numbers(my_numbers)
print(result)

