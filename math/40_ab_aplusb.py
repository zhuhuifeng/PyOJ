# coding=utf-8
# 给你两个整数a和b（-10000<a,b<10000），请你判断是否存在两个整数，他们的和为a，乘积为b。
# 若存在，输出Yes,否则输出No
# 例如：a=9,b=15, 此时不存在两个整数满足上述条件，所以应该输出No。

a,b = 9,15
delt=a*a-4*b
x1= int((a+delt**0.5)/2.0)
x2= int((a-delt**0.5)/2.0)
if x1+x2==a and x1*x2==b:
    print 'Yes'
else:
    print 'No'