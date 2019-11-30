su = list()
hap = 0

for i in range(5):
        su.append(int(input()))
        if su[i] < 40:
                su[i] = 40
        hap += su[i]

avg = hap // 5
print(avg)
