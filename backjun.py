n = int(input())
l = []
for i in range(n):
    l.append([*map(int,input().split())])
dp = [0] * n
for i in range(n):
    dp[i] = l[i][0]
    for j in range(n):
        if j == 0:
            dp[i] = max(dp[i], dp[i] + l[i][j], dp[i] + l[i][j + 1])
        elif j == n - 1:
            dp[i] = max(dp[i], dp[i] + l[i][j], dp[i] + l[i][j - 1])
        else:
            dp[i] = max(dp[i], dp[i] + l[i][j], dp[i] + l[i][j - 1], dp[i] + l[i][j + 1])
print(dp)