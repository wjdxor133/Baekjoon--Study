Attendance = [1,2,3,4,5,6,7,8,9,10,
              11,12,13,14,15,16,17,
              18,19,20,21,22,23,24,
              25,26,27,28,29,30]
i = 0
while i < 29:
        a = int(input())
        for i in range(len(Attendance)):
                for j in Attendance:
                        if j == a:
                                Attendance.remove(j)
        i += 1
for i in range(len(Attendance)):
        print(Attendance[i])
