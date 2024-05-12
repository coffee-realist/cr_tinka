from sys import stdin, stdout
from math import inf

input = stdin.readline
ln, n = map(int, input().split())
lst = [0] + list(map(int, input().split())) + [ln]
n += 2
dp = [[0] * n for _ in range(n)]
for cur_ln in range(2, n):
    for i in range(n - cur_ln):
        j = i + cur_ln
        dp[i][j] = inf
        for k in range(i + 1, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + lst[j] - lst[i])
stdout.write(f'{dp[0][n - 1]}')
