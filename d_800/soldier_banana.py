nums = input().split()

price = int(nums[0])
dollars = int(nums[1])
banana = int(nums[2])

count = 1
total = 0

while banana > 0:
    total = total + (price*count)
    count += 1
    banana -= 1


if total <= dollars:
    print(0)
else:
    print(total - dollars)

