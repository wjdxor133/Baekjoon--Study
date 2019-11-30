su = list()
hap = 0
for i in range(4):
    su.append(int(input()))
    hap += su[i]
a, b= divmod(hap, 60)
print(a), print(b)
