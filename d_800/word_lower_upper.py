word = input()

lower_count = 0
upper_count = 0

for char in word:
    if char == char.lower():
        lower_count += 1
    else:
        upper_count += 1


if lower_count >= upper_count:
    print(word.lower())
else:
    print(word.upper())