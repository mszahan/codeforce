nums = [4, 3, 1, 2, 5, 8, 7]
# nums_copy = [4, 3, 1, 2, 5, 8, 7]
nums_copy = nums[:]

nums[0] =5

sorted_list = [None]*len(nums)
count = 0

for num in nums:
    for cnum in nums_copy[count+1:]:
        if cnum < num:
            sorted_list[count] = cnum
        elif sorted_list[count] != None and sorted_list[count]      
        else:
            sorted_list[count] = num

    count += 1

# print(sorted_list[0])

print(sorted_list)