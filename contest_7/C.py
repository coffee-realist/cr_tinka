from collections import deque

n, k = map(int, input().split())
coins = [0] + list(map(int, input().split())) + [0]
dp = [0] * n
path = [-1] * n
dq = deque([0])
for i in range(1, n):
    while dq and dq[0] < i - k:
        dq.popleft()
    dp[i] = dp[dq[0]] + coins[i]
    path[i] = dq[0]
    while dq and dp[i] >= dp[dq[-1]]:
        dq.pop()
    dq.append(i)
result_path = []
point = n - 1
while point >= 0:
    result_path.append(point + 1)
    point = path[point]
result_path.reverse()
print(dp[n - 1])
print(len(result_path) - 1)
print(' '.join(map(str, result_path)))
'''
5 3
2 -3 5

12 5
-5 -4 -3 -2 -1 1 2 3 4 5

10 3
-13 -2 -14 -124 -9 -6 -5 -7

'''
