# coding=utf-8
# 给你两个正整数a(0 < a < 100000)和n(0 <= n <=100000000000)，计算(a^n) % 20132013并输出结果

a,n = 23456,10000000

def ModExp(a, n):
    ans = 1
    while n:
        if n % 2:
            ans = (ans * a) % 20132013
        n = n // 2
        a = (a * a) % 20132013
    return ans


print ModExp(a, n)
