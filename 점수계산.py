score = list()
five_score = list()
total = 0

for i in range(8):
    score.append(int(input()))
copy_score = score[:]
for i in range(5):
    su = max(copy_score)
    copy_score.remove(su)
    total += su
    for j in score:
        if su == j:
            num = score.index(su)
            five_score.append(num+1)
print(total)
for i in sorted(five_score):
    print("%s " % i, end ="")
            
    
