# coding=utf-8
#给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','链接，如‘1,2,3'。

a = {1:1, 2:2, 3:3}
print ','.join([str(k) for k in a.keys()])