url = 'https://docs.python.org/3/tutorial'
w1_f = url.find('ht')
w1_e = url.rfind(':')
w2_f = url.find('do')
w2_e = url.rfind('/3')
w3_f = url.find('tu')


print(url[w1_f:w1_e])
print(url[w2_f:w2_e])
print(url[w3_f:])

