import sys
input = sys.stdin.readline
INF = int(1e9)
te = int(input())

for _ in range(te):
    necy = 0
    n, m, w = map(int, input().split())
    shop = [[] for i in range(n + 1)]
    for i in range(m):
        s, e, t = map(int, input().split())
        shop[s].append((e, t))
        shop[e].append((s, t))
    for i in range(w):
        s ,e ,t = map(int, input().split())
        shop[s].append((e, -t))
    dist = [INF] * (n + 1)
    dist[1] = 0
    for i in range(n):
        for j in range(1, n + 1):
            for x, d in shop[j]:
                if dist[x] > dist[j] + d: # dist[x] != INF 조건을 넣으면 처음 방문한 노드에서 음수사이클 여부 판별 가능하나 없으면 모든 노드에서의 음수사이클 여부 확인 가능
                    dist[x] = dist[j] + d
                    if i == n - 1:
                        necy = 1
    if necy:
        print("YES")
    else:
        print("NO")
