from random import randint
su = [0,0,0]
for i in range(3):
    su[i] = randint(1,99)
big = max(su[0],su[1],su[2])
print('{} {} {} 중에서 최대 : {}'.format(su[0], su[1], su[2], big))
