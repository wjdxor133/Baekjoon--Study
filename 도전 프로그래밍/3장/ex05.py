time = input('시각 정보(16:30:15) 입력 >>')
t1, t2, t3 = time.split(':')
print('%d시 %d분 %d초' % (int(t1),int(t2),int(t3)))

