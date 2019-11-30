su = int(input())
ability = list()
total = list()
i = 0
while i < su:
    ability[:] = input().split()
    j = 0
    HP = int(ability[j]) + int(ability[j+4])
    MP = int(ability[j+1]) + int(ability[j+5])
    attack = int(ability[j+2]) + int(ability[j+6])
    if HP < 1:
        HP = 1
    if MP < 1:
        MP = 1
    if attack < 0:
        attack = 0
    result = 1 * (HP) + 5 * (MP) + 2 * (attack) + 2 * (int(ability[j+3]) + int(ability[j+7]))
    total.append(result)
    i += 1
for i in range(su):
    print(total[i])
