data = input().split()

width = int(data[0])
height = int(data[1])
square_height = int(data[2])

def round_number(num):
    if num > int(num):
        return int(num) + 1
    return num
    
width_round = round_number(width/square_height)
height_round = round_number(height/square_height)


result = width_round * height_round
print(int(result))