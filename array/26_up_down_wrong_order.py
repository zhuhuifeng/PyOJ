# coding=utf-8
# 给你一个整数组成的列表L，按照下列条件输出：
# 若L是升序排列的,则输出"UP";
# 若L是降序排列的,则输出"DOWN";
# 若L无序，则输出"WRONG"。
L = [1,3,4,5,7]
up_i, down_i = 0, 0
for i in range(1, len(L) - 1):
    if L[i] >= L[i - 1] and L[i + 1] >= L[i] and up_i == i - 1:
        up_i = i
    if L[i] <= L[i - 1] and L[i + 1] <= L[i] and down_i == i - 1:
        down_i = i

if up_i == len(L) - 2:
    print 'UP'
elif down_i == len(L) - 2:
    print 'DOWN'
else:
    print 'WRONG'
