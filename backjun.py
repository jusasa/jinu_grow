import sys, heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
l = [[] for i in range(n + 1)]
for i in range(m):
    x, y, c = map(int, input().split())
    l[x].append((y, c))
    
dist = [float('inf') for i in range(n + 1)]
visited = [False for i in range(n + 1)]
prev = [-1 for i in range(n + 1)]

x, y = map(int, input().split())
dist[x] = 0
st = []
heapq.heappush(st, (0, x))
while st:
    d, v = heapq.heappop(st)
    if visited[v]:
        continue
    visited[v] = True
    for i in l[v]:
        if dist[i[0]] > dist[v] + i[1]:
            dist[i[0]] = dist[v] + i[1]
            prev[i[0]] = v
            heapq.heappush(st, (dist[i[0]], i[0]))

path = []
current = y
while current != -1:
    path.append(current)
    current = prev[current]
print(dist[y]) 
print(len(path))
print(*path[::-1])    
