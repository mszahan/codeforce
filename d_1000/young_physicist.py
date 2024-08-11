n = int(input())
matrix = []

while n > 0:
    row = input().split()
    row_int = [int(num) for num in row]
    matrix.append(row_int)
    n -= 1

x = 0
y = 0
z = 0

for row in matrix:
    x += row[0]
    y += row[1]
    z += row[2]


if x == 0 and y == 0 and z ==0:
    print('YES')
else:
    print('NO')


