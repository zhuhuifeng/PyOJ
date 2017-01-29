# coding=utf-8
# 给你三个整数a,b,c,  判断能否以它们为三个边长构成三角形。
# 若能，输出YES，否则输出NO。

a,b,c = 3,4,5
L = [a,b,c]
L.sort()
if (L[0]+L[1]>L[2]):
    print 'YES'
else:
    print 'NO'