from random import randint
su = [0,0]
for i in range(2):
    su[i] = randint(1,99)
print('%d * %d = %d' % (su[0], su[1], su[0] * su[1]))
while True:
    str = input('계속 y / n ? ')
    if str == 'y':
        for i in range(2):
            su[i] = randint(1,99)
        print('%d * %d = %d' % (su[0], su[1], su[0] * su[1]))
    if str == 'n':
        break
    
