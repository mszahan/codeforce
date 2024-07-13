mat = []
loop = 5
while loop > 0 :
    row = input().split()
    mat.append(row)
    loop -= 1


indx_of_one = []
row_count = 0

for row in mat:
    if '1' in row:
        indx_of_one = [row_count, row.index('1')]
    else:
        row_count += 1


result = abs(indx_of_one[0] -2 ) + abs(indx_of_one[1] -2)
print(result)


# print(indx_of_one)

# mat = ['1', '0', '0']
# indx = mat.index('1')
# print(indx, type(indx))