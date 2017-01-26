# coding=utf-8
#给你一个list L, 如 L=[0,1,2,3,4], 输出L的中位数（若结果为小数，则保留一位小数）。

def FormatOut(ans):
    if ans % 1 == 0 :
        return ans
    else :
        return round(ans, 1)

L = [3,1,2,4,5]
L.sort()
lLen = len(L)
if (lLen % 2) :
    print FormatOut(L[lLen/2])
else :
    print FormatOut((L[lLen/2-1] + L[lLen/2])/2.0)

print 1.5 % 1