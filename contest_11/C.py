from sys import stdin, stdout

input = stdin.readline
s = input()
n = len(s)
rev_s = s[::-1]
m = len(rev_s)
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j - 1] + 1 if s[i - 1] == rev_s[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
result = ''
i, j = n, m
while i > 0 and j > 0:
    if s[i - 1] == rev_s[j - 1]:
        result = s[i - 1] + result
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1
stdout.write(f'{dp[n][m]}\n')
stdout.write(f'{result}')
