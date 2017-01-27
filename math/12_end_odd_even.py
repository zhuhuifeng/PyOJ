# coding=utf-8
#给你一个正整数列表 L, 如 L=[2,8,3,50], 判断列表内所有数字乘积的最后一个非零数字的奇偶性,
#奇数输出1,偶数输出0. 如样例输出应为0

L = [2,8,3,50]
res = 1
for item in L:
    res *= item
    while not res % 10:
        res /= 10

print 1 if res % 2 else 0