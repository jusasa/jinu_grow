import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
a = [*map(int, input().split())]
m = int(input())

# Precompute palindrome information using DP
dp = [[False] * n for _ in range(n)]

# Single character substrings are palindromes
for i in range(n):
    dp[i][i] = True

# Two consecutive characters are palindromes if they are equal
for i in range(n - 1):
    if a[i] == a[i + 1]:
        dp[i][i + 1] = True

# Check for longer substrings
for length in range(3, n + 1):  # length of the substring
    for i in range(n - length + 1):
        j = i + length - 1  # endpoint of the substring
        if a[i] == a[j] and dp[i + 1][j - 1]:
            dp[i][j] = True

# Answer the queries
for _ in range(m):
    x, y = map(int, input().split())
    if dp[x - 1][y - 1]:
        print("1\n")
    else:
        print("0\n")
