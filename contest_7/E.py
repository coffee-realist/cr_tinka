s_1 = input()
s_2 = input()
dp = [[0] * (len(s_2) + 1) for _ in range(len(s_1) + 1)]
for i in range(len(s_1) + 1):
    dp[i][0] = i
for j in range(len(s_2) + 1):
    dp[0][j] = j
for i in range(1, len(s_1) + 1):
    for j in range(1, len(s_2) + 1):
        if s_1[i - 1] == s_2[j - 1]:
            price = 0
        else:
            price = 1
        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + price)
        if i > 1 and j > 1 and s_1[i - 1] == s_2[j - 2] and s_1[i - 2] == s_2[j - 1]:
            dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + price)
print(dp[len(s_1)][len(s_2)])
