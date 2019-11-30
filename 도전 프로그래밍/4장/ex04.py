h, w = input('당신의 키(cm)와 몸무게(kg)는? >> ').split()
h, w = int(h), int(w)
bmi = w / (h/100) ** 2
if bmi >= 40:
    print('키 : %d(cm), 몸무게: %d(km)' % (h, w))
    print('BMI: %.1f 고도 비만' % float(bmi))
elif 35 <= bmi:
    print('키 : %d(cm), 몸무게: %d(km)' % (h, w))
    print('BMI: %.1f 증등도 비만' % float(bmi))
elif 30 <= bmi:
    print('키 : %d(cm), 몸무게: %d(km)' % (h, w))
    print('BMI: %.1f 비만' % float(bmi))
elif 25<= bmi:
    print('키 : %d(cm), 몸무게: %d(km)' % (h, w))
    print('BMI: %.1f 과체중' % float(bmi))
elif 18.5 <= bmi:
    print('키 : %d(cm), 몸무게: %d(km)' % (h, w))
    print('BMI: %.1f 정상' % float(bmi))
else:
    print('키 : %d(cm), 몸무게: %d(km)' % (h, w))
    print('BMI: %.1f 저체중' % float(bmi))
