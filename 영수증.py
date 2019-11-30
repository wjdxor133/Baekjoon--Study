n_read = int(input())
b_price = list()
hap = 0

for i in range(9):
        b_price.append(int(input()))
        hap += b_price[i]
print(n_read - hap)
