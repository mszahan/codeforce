loop = int(input())
a = 0

while loop > 0:
    update = input()
    if update == '++X' or update == 'X++':
        a += 1
    else:
        a -=1
    loop -= 1

print(a)