# coding=utf-8
#给你两个正整数a和b， 输出它们的最大公约数。

def gcd(a, b):
    if (a < b):
       tmp = a
       a = b
       b = tmp
    if (a % b == 0):
        return b
    return gcd(b, a%b)


a = 21
b = 35

print gcd(a,b)
