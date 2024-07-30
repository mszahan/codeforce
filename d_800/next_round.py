n_k = input().split()
scores = input().split()

k = int(n_k[1])
count = 0
position_score = int(scores[k-1])

for score in scores:
    if int(score) >= position_score and int(score) !=0:
        count +=1

print(count)

