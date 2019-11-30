Ann = [500, 100, 50, 10, 5, 1]
money = int(input())
cnt = 0
result = 1000 - money
for i in Ann:
        cnt += int(result/i)
        result -= int(result/i)*i
print(cnt)
