# coding=utf-8
# 一个环形的公路上有n个加油站，编号为0,1,2,...n-1,
# 每个加油站加油都有一个上限，保存在列表limit中，即limit[i]为第i个加油站加油的上限，
# 而从第i个加油站开车开到第(i+1)%n个加油站需要cost[i]升油,cost为一个列表。
# 现在有一辆开始时没有油的车，要从一个加油站出发绕这个公路跑一圈回到起点。
# 给你整数n，列表limit和列表cost,你来判断能否完成任务。
# 如果能够完成任务，输出起始的加油站编号，如果有多个,输出编号最小的。
# 如果不能完成任务，输出-1

limit = [3,4,5]
cost = [2,3,4]
n = 3

rest = [limit[i]-cost[i] for i in range(n)]

rest = rest[:]+rest[:]


for i in range(n):
    sign = True
    total = 0
    for j in range(n):
        total += rest[i+j]
        if total < 0:
            sign = False
            break
    if sign:
        pos = i
        break


if sign:
    print pos
else:
    print -1