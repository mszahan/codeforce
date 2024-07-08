loop = int(input())

number_of_solustion = 0

while loop > 0:
    num = input()
    n_num = num.split(' ')
    if n_num.count('1') >= 2:
        number_of_solustion += 1
    loop = loop -1

print(number_of_solustion)

# num = input()
# n_num = num.split(' ')

# print(n_num)