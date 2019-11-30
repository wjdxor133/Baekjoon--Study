from random import sample

a = set(sample(list(range(1,21)), 5))
b = set(sample(list(range(1,21)), 5))
print('A = {}'.format(a))
print('B = {}'.format(b))

print()

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a ^ b)


