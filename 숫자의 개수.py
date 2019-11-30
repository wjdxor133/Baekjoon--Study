su = list()
num = list()
cnt = 0
for i in range(3):
        su.append(int(input()))
gop = str(su[0] * su[1] * su[2])

for i in range(10):
        cnt = 0
        for j in gop:
                if int(j) == i:
                        cnt += 1
        num.append(cnt)
        print(num[i])
