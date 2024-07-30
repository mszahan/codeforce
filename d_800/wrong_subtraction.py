num_and_time = input().split()

num = int(num_and_time[0])
time = int(num_and_time[1])


while time > 0:
    if str(num)[-1] == '0':
        num = int(num / 10)
    else:
        num = num -1
    time -= 1


print(int(num))