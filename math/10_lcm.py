# coding=utf-8
# 给你两个整数a,b，输出他们的最小公倍数

def gcd(m, n):
    if (m < n):
        tmp = m
        m = n
        n = m
    if (not m%n):
        return n
    return gcd(n, m%n)

a, b = 45, 15
print a*b/gcd(a,b)