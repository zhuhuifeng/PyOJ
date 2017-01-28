# coding=utf-8
# 给你两个正整数a,b,  输出它们公约数的个数。

a,b = 14,56
print len([n for n in range(1, max(a,b)+1) if not a%n and not b%n])