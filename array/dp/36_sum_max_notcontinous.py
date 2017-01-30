# coding=utf-8
# 给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个非连续子序列，使其和最大，输出最大子序列的和。
# 这里非连续子序列的定义是，子序列中任意相邻的两个数在原序列里都不相邻。
# 例如，对于L=[2,-3,3,50]， 输出52（分析：很明显，该列表最大非连续子序列为[2,50]).


L=[2,-3,3,50]

def maxSum(L):
    size = len(L)
    s = [0]*size
    s[0] = L[0]
    s[1] = L[1]
    rsl = max(s[0], s[1])
    for i in range(2, size):
        s[i] = max(max(s[0:i-1]) + L[i], L[i])
        if s[i] > rsl:
            rsl = s[i]
    return rsl
print maxSum(L)