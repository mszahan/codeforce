word = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

final_word = ''


for char in word:
    if char not in vowels:
        final_word += f".{char}"

print(final_word)