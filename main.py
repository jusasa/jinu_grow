r, c, k = map(int, input().split())

board = [[*map(str, input())] for i in range(r)]
visited = [[0] * c for i in range(r)]
def dfs(x, y, depth):
    co = 0
    if depth == k:
        if x == c - 1 and y == 0:
            co += 1
            return co
        else:
            return 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < c and 0 <= ny < r and board[ny][nx] == '.' and not visited[ny][nx]:
            visited[ny][nx] = 1
            co += dfs(nx, ny, depth + 1)
            visited[ny][nx] = 0
    return co
visited[r - 1][0] = 1
result = dfs(0, r - 1, 1)
print(result)