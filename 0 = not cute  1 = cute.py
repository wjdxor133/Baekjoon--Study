su = int(input())
team = list()
v_cute = list()
Y_cute, N_cute = 0,0
for i in range(su):
        v_cute.append(int(input()))
        if v_cute[i] == 1:
                Y_cute += 1
        else:
                N_cute += 1      
if N_cute > Y_cute:
        print("Junhee is not cute!")
else:
        print("Junhee is cute!")
