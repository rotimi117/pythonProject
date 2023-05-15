def elements_even_positions(lst):
    even_elements = lst[::2]
    return even_elements

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_elements = elements_even_positions(my_list)
print(even_elements)
