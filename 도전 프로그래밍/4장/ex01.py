month = int(input('월 입력 ?' ))
if (month == 3 or month == 2 or month == 1 or month == 12 or month ==11):
    print("%d월 겨울" % month)
elif (month == 9 or month ==10):
    print("%d월 가울" % month)
elif (month == 8 or month == 7 or month == 6):
    print("%d월 여름" % month)
else:
    print("%d월 봄" % month)
