su1 ,g, su2 = input().split(" ")
if g == '+':
	print('%d' % (int(su1) + int(su2)))
elif g == '-':
	print('%d' % (int(su1) - int(su2)))
elif g == '*':
	print('%d' % (int(su1) * int(su2)))
elif g == '/':
	print('%.2f' % (int(su1) / int(su2)))
