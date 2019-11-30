L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())
math = 0
korean = 0
if A%C == 0:
    math = int(A/C)
else:
    math = int(A/C + 1) 
if B%D == 0:
    korean = int(B/D)
else:
    korean = int(B/D + 1)
if math > korean:
    print(L-math)
else:
    print(L-korean)
