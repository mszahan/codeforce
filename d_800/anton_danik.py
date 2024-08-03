game_nums = input()
games = input()

anton = 0
danik = 0


for player in games:
    if player == 'A':
        anton += 1
    else:
        danik += 1


if anton > danik:
    print('Anton')

elif anton == danik:
    print('Friendship')

else:
    print('Danik')
