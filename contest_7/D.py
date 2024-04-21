n, m = [cur + 2 for cur in list(map(int, input().split()))]
dp = [[0] * 20 for _ in range(20)]
dp[2][2] = 1
i, j = 2, 2
while i < n - 1 or j < m - 1:
    x, y = i, j
    while x >= 2 and y < m:
        dp[x][y] += dp[x - 2][y - 1] + dp[x - 2][y + 1] + dp[x - 1][y - 2] + dp[x + 1][y - 2]
        x -= 1
        y += 1
    if i == n - 1:
        j += 1
    else:
        i += 1
x, y = n - 1, m - 1
dp[n - 1][m - 1] += dp[x - 2][y - 1] + dp[x - 2][y + 1] + dp[x - 1][y - 2] + dp[x + 1][y - 2]
print(dp[n - 1][m - 1])
