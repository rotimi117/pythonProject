def combine_lists_alternatively(list1, list2):
    combined_list = []
    min_len = min(len(list1), len(list2))
    for i in range(min_len):
        combined_list.append(list1[i])
        combined_list.append(list2[i])
    if len(list1) > len(list2):
        combined_list.extend(list1[min_len:])
    elif len(list2) > len(list1):
        combined_list.extend(list2[min_len:])

    return combined_list

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
combined = combine_lists_alternatively(list1, list2)
print(combined)
