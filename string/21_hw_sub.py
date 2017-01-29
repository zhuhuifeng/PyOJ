# coding=utf-8
# 给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。

a,n = '1345654',5
def isok(s):
    mindex = len(s)//2
    for i in range(0, mindex):
        if s[i] != s[len(s)-1-i]:
            return False
    return True
hw = False
for i in range(0, len(a)+1-n):
    st = a[i:i+n]
    hw = isok(st)
    if hw:
        break
if not hw:
    print "NO"
else:
    print "YES"