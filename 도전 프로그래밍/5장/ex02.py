korean = ('정렬', '초보자', '내포', '사전')
english = ('sorting', 'novice', 'comprehension', 'dictionary')

str = input('찾을 단어 입력 ? ')
for i in korean: # korean에 있는  i를 순서대로 담아서
    if str == i: # 입력한 str과 i가 같으면 
        su = korean.index(i) #korean에 있는 리스트에 해당하는 인덱스를 추출한다
        print('{}'.format(english[su])) # 대응되는 english의 값을 출력한다
    else:
        print('사전에 없는 단어입니다.')
        break
    
