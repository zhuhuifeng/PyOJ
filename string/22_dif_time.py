#coding=utf-8
# 给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 请你给出这两个时间间隔的秒数。
# 如：st="00:00:00", et="00:00:10", 则输出10.

st,et = '12:34:45','14:45:12'
(sth,stm,sts) = st.split(":")
(eth,etm,ets) = et.split(':')

print int(eth)*3600+int(etm)*60+int(ets)-int(sth)*3600-int(stm)*60-int(sts)