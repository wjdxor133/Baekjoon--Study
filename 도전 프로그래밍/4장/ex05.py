for c in range(20,42):
    f = c *9/5+32
    s = c *2 + 30
    cha = f - s
    result = abs(cha)
    print('섭씨: %d 화씨: %.1f 화씨(약식): %d 차이: %.2f' % (c,f,s,result))
