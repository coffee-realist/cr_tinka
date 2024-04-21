def longest_valid_subsequence(left, right):
    if left > right:
        return
    if left == right:
        result[right] = '/'
        return
    if dp[left][right] == dp[left][right - 1] + 1:
        result[right] = '/'
        longest_valid_subsequence(left, right - 1)
        return
    for k in range(left, right):
        if closing_bracket[ord(s[right])] == s[k]:
            if k == left:
                if dp[left][right] == dp[left + 1][right - 1]:
                    longest_valid_subsequence(left + 1, right - 1)
                    return
            elif dp[left][right] == dp[left][k - 1] + dp[k][right]:
                longest_valid_subsequence(left, k - 1)
                longest_valid_subsequence(k, right)
                return


s = input()
n = len(s)
dp = [[0] * n for _ in range(n)]
result = ['.'] * n
closing_bracket = ['.' for _ in range(600)]
closing_bracket[ord(')')] = '('
closing_bracket[ord(']')] = '['
closing_bracket[ord('}')] = '{'
for i in range(n):
    dp[i][i] = 1
for i in range(1, n + 1):
    for j in range(n):
        if j + i >= n:
            break
        cur_left = j
        cur_right = j + i
        dp[cur_left][cur_right] = dp[cur_left][cur_right - 1] + 1
        for sp in range(cur_left, cur_right):
            if closing_bracket[ord(s[cur_right])] == s[sp]:
                if sp == cur_left:
                    dp[cur_left][cur_right] = min(dp[cur_left][cur_right], dp[cur_left + 1][cur_right - 1])
                else:
                    dp[cur_left][cur_right] = min(dp[cur_left][cur_right],
                                                  dp[cur_left][sp - 1] + dp[sp][cur_right])
longest_valid_subsequence(0, n - 1)
for i in range(n):
    if result[i] == '.':
        print(s[i], end='')
