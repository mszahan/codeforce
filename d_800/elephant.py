coordinate = int(input())


if coordinate <=5:
    print(1)
elif coordinate % 5 ==0:
    print(int(coordinate/5))
else:
    result = int(coordinate / 5) + 1
    print(result)

