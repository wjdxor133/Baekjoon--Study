su = int(input())
result = list()
for i in range(su):
        r, e, c = map(int,input().split())
        if (e - r) > c:
            result.append("advertise")
        elif (e - r) == c:
            result.append("does not matter")
        elif (e - r) < c:
            result.append("do not advertise")

for i in range(len(result)):
    print(result[i])
