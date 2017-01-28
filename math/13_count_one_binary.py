# coding=utf-8
# 给你一个整数a，数出a在二进制表示下1的个数，并输出。

a = 34
res = 0
while a:
    if a%2:
        res += 1
    a //= 2
print res