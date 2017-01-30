# coding=utf-8
# 给以一个三角形的三边长a,b和c(边长是浮点数),请你判断三角形的形状。
# 若是锐角三角形，输出R,
# 若是直角三角形，输出Z，
# 若是钝角三角形，输出D，
# 若三边长不能构成三角形，输出W.

a,b,c = 2,3,4

L = [a,b,c]
L.sort()
cos_value = 999
if L[2] < L[1]+L[0]:
    cos_value = (L[1]**2 + L[0]**2 - L[2]**2)/2*L[1]*L[0]

if cos_value > 0 and cos_value < 1:
    print 'R'
elif not cos_value:
    print 'Z'
elif cos_value <0:
    print 'D'
else:
    print 'W'