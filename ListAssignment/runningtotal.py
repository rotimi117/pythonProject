def compute_running_total(lst):
    running_total = 0
    result = []
    for element in lst:
        running_total += element
        result.append(running_total)
    return result

my_list = [1, 2, 3, 4, 5]
running_total = compute_running_total(my_list)
print(running_total)
