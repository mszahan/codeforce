number_of_coins = int(input())
coins = input().split()

coins = [int(coin) for coin in coins]
coins.sort(reverse=True)

count = 1

while count <= number_of_coins:
    if sum(coins[:count]) > sum(coins[count:]):
        break
    else:
        count += 1


print(count)