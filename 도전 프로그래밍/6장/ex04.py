fruits = ['apple', 'banana', 'grapes', 'pear']
prices = (1000, 500, 1200, 1500)
z = dict(zip(fruits,prices))
# zip()을 이용해 fruits와 prices을 하나의 튜플로 만든 후, dict() 함수를 이용해 딕셔너리로 형변환 
print(z)
print()

for name,i in enumerate(z): # enumerate()는 0부터 시작하는 첨자와 항목을 매칭시켜 튜플 리스트를 생성한다 즉, name에는 첨자, i에는 키 값이 참 
    print('{} 가격: {}'.format(fruits[name],z[i]))
