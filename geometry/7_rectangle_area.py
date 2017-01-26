# coding=utf-8
#已知矩形长a,宽b,输出其面积和周长，面积和周长以一个空格隔开

a = 12
b = 20

print ' '.join([str(a*b), str(2*a+2*b)])
print ' '.join(['%d' % x for x in [a*b, 2*a+2*b]])