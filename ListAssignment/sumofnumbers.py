def for_loop(list1):
    total = 0
    for num in list1:
        total += num
    return total

def while_loop(list1):
    total = 0
    index = 0
    while index < len(list1):
        total += list1[index]
        index += 1
    return total

def do_while_loop(list1):
    total = 0
    index = 0
    if len(list1) > 0:
        while True:
            total += list1[index]
            index += 1
            if index >= len(list1):
                break
    return total

my_list = [5, 6, 7, 8, 9]
print(for_loop(my_list))
print(while_loop(my_list))
print(do_while_loop(my_list))
