data = [[1,2,3],
        [4,5,6],
        [7,8,9]]

csum = list()
rsum = list()

for i in data:
    sum = 0
    for j in i:
        sum = sum + j
    csum.append(sum)
print('각 행의 합:', csum)

for i in range(3):
    sum = 0
    for j in range(3):
        r = data[j][i]
        sum = sum + r
    rsum.append(sum)
print('각 열의 합:', rsum)
        
        
        
        
        
        
