from random import randint
su = randint(1,100)
print('첫 값은 %d이다.' % su)
exp = list('+-*/%')
while True:
    ex = input('산술 연산의 종류를 입력하세요. >> ')
    if ex not in exp:
        print('종료'. center(20,'*'))
        break
    su2 = int(input('두 번째 피연산자를 입력하세요. >>' ))
    if ex in exp:
        if ex == '+':
            print('{} {} {} = {}'.format(su, ex, su2, su + su2))
            print()
        elif ex == '-':
            print('{} {} {} = {}'.format(su, ex, su2, su - su2))
            print()
        elif ex == '*':
            print('{} {} {} = {}'.format(su, ex, su2, su * su2))
            print()
        elif ex == '/':
            print('{} {} {} = {}'.format(su, ex, su2, su / su2))
            print()
        else:
            print('{} {} {} = {}'.format(su, ex, su2, su % su2))
            print()
        

    
    
    
