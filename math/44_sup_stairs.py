# coding=utf-8
# 有一楼梯共n级，刚开始时你在第一级，若每次只能跨上一级或二级，要走上第n级，共有多少种走法？
# 现在给你一个正整数n（0<n<40),请你输出不同的走法数。
# 如n=2,则输出1（你只有一种走法，走一步，从第一级到第二级）

n = 12

f2 = 1
f3 = 2

for i in range(4, n+1):
    res = f2 + f3
    f2,f3 = f3, res

if n == 2:
    print 1
elif n == 3:
    print 2
else:
    print res