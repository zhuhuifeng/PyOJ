# coding=utf-8
# 给你一个整数列表L,判断L中是否存在相同的数字，
# 若存在，输出YES，否则输出NO。

L = [34,56,78,90,23,45,56]
L.sort()
flag = False
for i in range(0,len(L)-1):
    if L[i] == L[i+1]:
        flag = True
        break
print 'YES' if flag else 'NO'