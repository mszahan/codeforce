word = input()
word_to_check = input()


reveresed_word = ''

count = len(word)-1

while count >= 0:
    reveresed_word += word[count]
    count -= 1

if reveresed_word == word_to_check:
    print('YES')
else:
    print('NO')

