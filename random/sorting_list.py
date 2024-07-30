# num_list = [5, 5, 6, 3, 3, 5, 2, 1]


# sorted_list = []

# while len(num_list) > 0:
#     first_num = num_list[0]
#     for num in num_list[1:]:
#         if first_num > num:
#             first_num = num
#     num_list.remove(first_num)
#     sorted_list.append(first_num)

n_list = input().split()
flist = [int(num) for num in n_list]

def sort_list(num_list):
    sorted_list = []
    while len(num_list) > 0:
        first_num = num_list[0]
        for num in num_list[1:]:
            if first_num > num:
                first_num = num
        num_list.remove(first_num)
        sorted_list.append(first_num)
    return sorted_list

# print(num_list)
# print(sorted_list)

# num_list.remove(5)
# print(num_list)

print(sort_list(flist))