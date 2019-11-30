m = [[1,2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in m] for i in range(len(m[0]))]

print(transpose)
print()
print('트랜스포즈를 for문으로 출력')
for i in range(len(m[0])):
    for row in range(len(m)):
        print('%d' % m[row][i], end = ' ')
    print()
