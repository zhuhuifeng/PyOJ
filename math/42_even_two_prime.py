# coding=utf-8
# 把一个偶数拆成两个不同素数的和，有几种拆法呢？
# 现在来考虑考虑这个问题，给你一个不超过10000的正的偶数n，
# 计算将该数拆成两个不同的素数之和的方法数，并输出。
# 如n=10，可以拆成3+7，只有这一种方法，因此输出1.

n = 10

su_shu = [ y for y in range(2, n) if not [ x for x in range(2, y) if not y%x]]
res = 0
for i in range(0, len(su_shu)):
    if n - su_shu[i] in su_shu[i+1:]:
        res += 1

print res

