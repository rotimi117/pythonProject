def element_in_list(lst, element):
    return element in lst

my_list = [10, 8, 9, 7, 5]
element_to_check = 10

if element_in_list(my_list, element_to_check):
    print(f"The element {element_to_check} is present in the list.")
else:
    print(f"The element {element_to_check} is not present in the list.")
