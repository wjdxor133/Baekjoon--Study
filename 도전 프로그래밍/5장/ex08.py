from random import randint
lst = list()
sum = 0
cnt = 0

for i in range(10):
    su = (randint(1,99))
    lst.append(su)
print('리스트 :', lst)
print('튜플 : ' , tuple(lst))
n_lst = sorted(lst)
print('튜플 정렬된 리스트 : ', n_lst)

for i in range(len(n_lst)):
    sum = sum + n_lst[i]
    cnt = cnt + 1
print('합 : %d, 항목수 : %d' % (sum, cnt))
print('최대 : %d, 최소 : %d, 평균 : %.2f' %(max(n_lst), min(n_lst), sum/cnt))

    
