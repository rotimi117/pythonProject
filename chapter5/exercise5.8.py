def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


import random
nums = random.sample(range(101), 10)

print("Unsorted List:", nums)

sorted_nums = insertion_sort(nums)

print("Sorted List:", sorted_nums)
