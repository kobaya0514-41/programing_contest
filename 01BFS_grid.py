from collections import deque

#input
H,W = map(int,input().split())

#start and goal
rs,cs = map(int,input().split())
rt,ct = map(int,input().split())

#distance from start
dist = [[10**9]*W for i in range(H)]

#01BFS
que = deque()
que.append((rs,cs))

while len(que) > 0:
    i, j = que.popleft()
    
    for i2, j2 in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
        if not (0 <= i2 < H and 0 <= j2 < W):
            continue
            
        # operation
        new_distance = dist[i][j] + ??
        #update
        if new_distance < dist[i2][j2]:
            dist[i2][j2] = new_distance
            if (operation_0):
                que.appendleft((i2,j2))
            else:
                que.append((i2,j2))
