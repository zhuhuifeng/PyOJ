# coding=utf-8

#给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。
#输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。

import math
a,b = 12,36
if a > b:
    a, b = b, a
p = b / a
for i in range(1, int(math.sqrt(p)) + 1):
    if p % i == 0:
        f1, f2 = i, p / i

print f1 * a, f2 * a