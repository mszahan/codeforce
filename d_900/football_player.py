all_players = input()

zero_danger = '0000000'
one_danger = '1111111'

if zero_danger in all_players or one_danger in all_players:
    print('YES')

else:
    print('NO')