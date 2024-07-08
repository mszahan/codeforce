number_of_loop = int(input())

while number_of_loop > 0:
    word = input()

    if len(word) > 10:
        first_char = word[0]
        last_char = word[-1]
        print(f"{first_char}{len(word)-2}{last_char}")
    else:
        print(word)
    number_of_loop = number_of_loop - 1