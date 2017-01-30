# coding=utf-8
# 给你一个字符串列表L，请用一行代码将列表所有元素拼接成一个字符串并输出。
# 如L=['abc','d','efg'], 则输出abcdefg。

L=['abc','d','efg']
print ''.join(L)

# 给你一个字符串列表L，用一行代码顺序输出L中的元素，元素之间以一个空格隔开，注意行尾不要有空格，输出单独占一行。
# 如L=['abc','d','efg'], 则输出abc d efg。
print ' '.join(L)