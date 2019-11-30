from random import randint
Lst = list()
for i in range(10):
    lst = randint(1,99)
    Lst.append(lst)
print(Lst)
print(sorted(Lst))
print(sorted(Lst,reverse=True))
# sort()는 그 리스트 자체에서 정렬
# sorted()는 리스트를 정렬 후 새로운 리스트로 반환 >> 원래 리스트에는 영향을 주지 않음
    
