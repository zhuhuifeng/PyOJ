# coding=utf-8
# 给你一个正整数列表 L, 如 L=[2,8,3,50], 输出L内所有数字的乘积末尾0的个数,
# 如样例L的结果为2.(提示:不要直接相乘,数字很多,可能溢出)

L = [2,8,3,50]
n0, n2, n5 = 0, 0, 0
for item in L:
    while not item%10:
        n0+=1
        item /= 10
    while not item%5:
        n5+=1
        item /= 5
    while not item%2:
        n2+=1
        item /= 2

print (n0+n5) if (n2 > n5) else (n0+n2)