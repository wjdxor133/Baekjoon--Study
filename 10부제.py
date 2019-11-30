day = input()
car_num = list()
car_num.append(input().split())
cnt = 0
for j in car_num[0]:
        if day == j:
                cnt += 1                        
print(cnt)
