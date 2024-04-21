n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
mx = 0
x, y = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            if dp[i][j] > mx:
                mx = dp[i][j]
                x, y = i - mx + 1, j - mx + 1
print(mx)
print(x + 1, y + 1)
