both_weight = input().split()

limak_weight = int(both_weight[0])
bob_weight = int(both_weight[1])

count = 0

while limak_weight <= bob_weight:
    limak_weight = limak_weight * 3
    bob_weight = bob_weight *2
    count += 1

print(count)
