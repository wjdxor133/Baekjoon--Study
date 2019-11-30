buger = list()
juice = list()
price = list()

for i in range(3):
        buger.append(int(input()))
for i in range(2):
        juice.append(int(input()))

for i in range(3):
        for j in range(2):
                b_set = buger[i] + juice[j]
                price.append(b_set)
print(min(price) - 50)
