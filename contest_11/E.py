from sys import stdin, stdout, setrecursionlimit
from math import inf, log10

setrecursionlimit(10 ** 5)


def get_digits(x):
    return 1 if x == 0 else int(log10(abs(x))) + 1


def compress(x, y):
    if x == y:
        return s[x]
    size = y - x + 1
    for k in range(1, size // 2 + 1):
        if size % k != 0:
            continue
        unbroken = True
        for d in range(k):
            for idx in range(x + d, y + 1, k):
                if s[x + d] != s[idx]:
                    unbroken = False
                    break
        if unbroken:
            cur_size = get_digits(size // k) + 2 + dp[x][x + k - 1]
            if cur_size == dp[x][y]:
                return f"{size // k}({compress(x, x + k - 1)})"
    for k in range(x, y):
        if dp[x][k] + dp[k + 1][y] == dp[x][y]:
            return compress(x, k) + compress(k + 1, y)


s = stdin.readline().strip()
n = len(s)
dp = [[0 for _ in range(n)] for _ in range(n)]
for ind in range(n):
    for i in range(n):
        j = i + ind
        if j >= n:
            break
        if ind == 0:
            dp[i][j] = 1
        else:
            mn = inf
            for step in range(1, (j - i + 1) // 2 + 1):
                if (j - i + 1) % step != 0:
                    continue
                flag = True
                for cur in range(step):
                    for pos in range(i + cur, j + 1, step):
                        if s[i + cur] != s[pos]:
                            flag = False
                            break
                if flag:
                    cur_len = get_digits((j - i + 1) // step) + 2 + dp[i][i + step - 1]
                    mn = min(mn, cur_len)
            for m in range(i, j):
                mn = min(mn, dp[i][m] + dp[m + 1][j])
            dp[i][j] = mn
stdout.write(compress(0, n - 1))
