username = input()

count = 0
char_list = []

for char in username:
    if char not in char_list:
        char_list.append(char)


if len(char_list) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
