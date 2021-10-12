#input
N,M = map(int,input().split())
 
#graph
G = []
for _ in range(N):
  G.append([])
 
#edge_information
for i in range(M):
  u,v,c = map(int,input().split())
  G[u - 1].append((v - 1,c))
  G[v - 1].append((u - 1,c))
 
#distance_from_No.0 
dist = [-1] * N
 
#dijkstra
Q = []
heapq.heappush(Q,(0,0))
dist[0] = 0
done = [False] * N
 
while len(Q) > 0 :
  d,i = heapq.heappop(Q)
  if done[i] :
    continue
 
  done[i] = True
 
  for (j,c) in G[i]:
    if dist[j] == -1 or dist[j] > dist[i] + c:
      dist[j] = dist[i] + c
      heapq.heappush(Q, (dist[j], j))
