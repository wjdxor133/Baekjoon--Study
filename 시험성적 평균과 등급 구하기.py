su = input()
su_sumList = su.split(' ')
su_sum = 0
for i in range(3):
    su_sum += int(su_sumList[i])

avg = float(su_sum/3)

if avg >= 90:
	print('{0:.2f} {1}'.format(avg,'A'))
elif avg >= 80:
	print('{0:.2f} {1}'.format(avg,'B'))
elif avg >= 70:
	print('{0:.2f} {1}'.format(avg,'C'))
elif avg >= 60:
	print('{0:.2f} {1}'.format(avg,'D'))
else:
	print('{0:.2f} {1}'.format(avg,'F'))
