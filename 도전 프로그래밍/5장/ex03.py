str = 'HelloPython!'
print('+ 012345678901')
print(str.rjust(14))
print('- 210987654321')
str = list(str)

while True:   
    su1, su2, su3 = map(int, input('슬라이스[?:?:?] 3개 입력 >> ').split())
    if su1 == 0 and su2 == 0 and su3 == 0:
        print('종료'.center(20,'*'))
        break
    print(str[su1:su2:su3])
    
    

