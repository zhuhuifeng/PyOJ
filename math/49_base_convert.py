# coding=utf-8
# 给你一个十进制数a，将它转换成b进制数,如果b>10,用大写字母表示（10用A表示，等等）
# a为32位整数，2 <= b <= 16
# 如a=3,b = 2, 则输出11

_base = '0123456789ABCDEF'
a,b = -3, 2
def tobase(num, base):
    if not num:
        return 0
    L = []
    while num:
        L.append(_base[num%base])
        num /= base
    res = ''.join(L[::-1])
    return res

print ('-' if a < 0 else '') + tobase(abs(a),b)