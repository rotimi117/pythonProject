egg_per_box = 6
total_eggs = 28
number_of_box = total_eggs // egg_per_box
last_box = total_eggs % egg_per_box
additional_egg = egg_per_box - last_box
print("number of boxes needed: ",number_of_box)
print("number of eggs in the last box:",last_box)
print("number of additional eggs",additional_egg)
