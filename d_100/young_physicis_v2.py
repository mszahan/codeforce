n = int(input())
matrix = []

while n > 0:
    row = input().split()
    row_int = [int(num) for num in row]
    matrix.append(row_int)
    n -= 1


sum_collections = {}


for row in matrix:
    x = len(row) - 1
    while x >= 0:
        if f'x_{x}' not in sum_collections:
            sum_collections[f'x_{x}'] = row[x]
        else:
            sum_collections[f'x_{x}'] += row[x]
        x -=1

# print(sum_collections.values())

non_zero_counter = []

for val in sum_collections.values():
    if val !=0:
        non_zero_counter.append(val)


if len(non_zero_counter) == 0:
    print('YES')
else:
    print('NO')
