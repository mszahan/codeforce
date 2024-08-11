players = input()

all_players = []

for player in players:
    all_players.append(int(player))

number_of_sequence = 7

found = ''

if len(all_players) >= number_of_sequence:
    loop = len(all_players) - number_of_sequence
    count = 0
    while count <= loop:
        collection = sum(all_players[count:count+number_of_sequence])
        if collection == 0 or collection == 7:
            found = 'YES'
        count += 1

if found == "YES":
    print('YES')
else:
    print('NO')
