# write a function that finds the most repeated item in a list

def find_most_repeated_item(lst):
    if not lst:
        return None

    item_count = {}
    max_count = 0
    most_repeated_item = None

    for item in lst:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

        if item_count[item] > max_count:
            max_count = item_count[item]
            most_repeated_item = item

    return most_repeated_item


my_list = [1, 2, 3, 4, 2, 3, 2, 2, 5, 5, 5, 1]
most_repeated = find_most_repeated_item(my_list)
print("Most repeated item:", most_repeated)
