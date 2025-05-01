import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
dist = [0] * 100001
visited = [False] * 100001
dq = deque()
dq.append(n)

while dq:
    x = dq.popleft()
    if x == k:  # 종료 조건
        print(dist[x])
        break
    for nx, cost in ((x - 1, 1), (x + 1, 1), (x * 2, 0)):
        if 0 <= nx < 100001 and not visited[nx]:
            visited[nx] = True  # 큐에 추가한 후 방문 처리
            if cost == 0:
                dq.appendleft(nx)
            else:
                dq.append(nx)
            dist[nx] = dist[x] + cost

#--------------------------------------------

from collections import deque
n,k=map(int,input().split())
limit=100001
cnt=[0]*limit
visited=[False]*limit
def bfs(x,end):
    queue=deque()
    queue.append(x)

    while queue:
        x=queue.popleft()
        if x==end:return cnt[x]
        if -1<x*2<limit and visited[x*2]==0 :
            queue.appendleft(x*2)
            cnt[x*2]=cnt[x]
            visited[x*2]=True
        if -1<x-1<limit and visited[x-1]==0 :
            queue.append(x-1)
            cnt[x-1]=cnt[x]+1
            visited[x-1]=True
        if -1<x+1<limit and visited[x+1]==0 :
            queue.append(x+1)
            cnt[x+1]=cnt[x]+1
            visited[x+1]=True



print(bfs(n,k))