from collections import deque
from math import inf


def min_digit_sum_divisible_by_k(k):
    if k == 1:
        return 1
    dp = [inf] * k
    d = deque()
    for i in range(1, 10):
        dp[i % k] = min(dp[i % k], i)
        d.append(i % k)
    while d:
        p = d.popleft()
        for digit in range(10):
            new_p = (p * 10 + digit) % k
            new_sum = dp[p] + digit
            if new_sum < dp[new_p]:
                dp[new_p] = new_sum
                d.append(new_p)
    if dp[0] != inf:
        return dp[0]
    else:
        return k


print(min_digit_sum_divisible_by_k(int(input())))
