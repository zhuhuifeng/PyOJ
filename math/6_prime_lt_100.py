# coding=utf-8
#输出100以内的所有素数，素数之间以一个空格区分

print ' '.join([str(x) for x in range(2, 100) if not [y for y in range(2, x) if not x%y]])
