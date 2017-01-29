# coding=utf-8
# 下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
# 棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.
# 如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。

m,n = 34,23
dx = ( 1, 2, 2, 1,-1,-2,-2,-1)
dy = (-2,-1, 1, 2, 2, 1,-1,-2)

def bfs(x,y):
    vis = [([0] * (m+1)) for i in range(n+2)]
    vis[x][y] = 1
    Q = [(x,y,0)]
    while Q:
        cur = Q.pop(0)
        if cur[0] == n and cur[1] == m: #finish
            return cur[2]
        for i in range(8):
            xt = cur[0] + dx[i]
            yt = cur[1] + dy[i]
            if xt < 0 or xt > n or yt < 0 or yt > m or vis[xt][yt]:
                continue
            vis[xt][yt] = 1
            Q.append((xt,yt,cur[2]+1))
    return -1

print(bfs(0,0))