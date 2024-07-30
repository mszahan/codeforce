num = int(input())
stons = input()

count = 0
neighbor = 0

while count < num-1:
    if stons[count] == stons[count+1]:
        neighbor += 1
    count += 1


print(neighbor)