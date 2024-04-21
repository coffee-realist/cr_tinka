def min_cost_to_top():
    dp = [0] * (n + 1)
    dp[1] = lst[0]
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1], dp[i - 2]) + lst[i - 1]
    return dp[n]


n = int(input())
lst = list(map(int, input().split()))
print(min_cost_to_top())
