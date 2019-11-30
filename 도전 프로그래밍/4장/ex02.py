from random import randint
i = 0
while i != 5:
    i = i+1
    time = randint(35,50)
    money = 12000
    week = time * money
    if time >= 40:
        bonus = (time * (money * 1.5))
        print('근로 시간 : %d시간, 주급 : %d' % (time,bonus))
    else:
        print('근로 시간 : %d시간, 주급 : %d' % (time,week))
    
