books = {'파이썬 개론': ['강환수'],
         'Perfect C': ['강환수', '이동규'],
         '컴퓨터 개론' : ['강환수', '조진형', '신용현']}
for i in books:
    valuse = list(books[i])
    print('책 이름: {}, 저자:'.format(i),  end = ' ')
    for j in valuse:
        print('{}'.format(j),  end = ' ')
    print()
