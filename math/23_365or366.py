# coding=utf-8
# 一年有多少天，这是个大问题，很值得思考。现在给你一个年份year(year为四位数字的字符串，如"2008","0012"),
# 你输出这一年的天数。如year="2013", 则输出365。

year = 2004
year = int(year)
flag = (not year%4 and year%100) or not year%400
print "366" if flag else "365"