n = int(input())
lst = list(map(int, input().split()))
dp = [1] * n
parents = [-1] * n
mx = 1
mx_ind = 0
for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            parents[i] = j
            if dp[i] > mx:
                mx = dp[i]
                mx_ind = i
result = []
while mx_ind != -1:
    result.append(lst[mx_ind])
    mx_ind = parents[mx_ind]
print(len(result))
print(*result[::-1])
