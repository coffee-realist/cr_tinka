from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict
from math import inf, log2

setrecursionlimit(10 ** 8)
input = stdin.readline


def lca(mx, v, u):
    result = inf
    if path[u] > path[v]:
        v, u = u, v
    for j in range(mx, -1, -1):
        if path[dp[v][j][0]] >= path[u]:
            result = min(result, dp[v][j][1])
            v = dp[v][j][0]
    if v == u:
        return result
    for j in range(mx, -1, -1):
        if dp[u][j][0] != dp[v][j][0]:
            result = min(result, dp[u][j][1])
            u = dp[u][j][0]
            result = min(result, dp[v][j][1])
            v = dp[v][j][0]
    return min(result, dp[v][0][1], dp[u][0][1])


def build(mx, v, p, c):
    if p != v:
        path[v] = path[p] + 1
    dp[v][0] = (p, c)
    for j in range(1, mx + 1):
        dp[v][j] = (dp[dp[v][j - 1][0]][j - 1][0], min(dp[v][j - 1][1], dp[dp[v][j - 1][0]][j - 1][1]))
    for next_v, next_c in graph[v]:
        build(mx, next_v, v, next_c)


n = int(input())
graph = defaultdict(list)
for i in range(1, n):
    x, y = map(int, input().split())
    graph[x].append((i, y))
dp = [[(0, 0)] * (max(1, int(log2(n))) + 1) for _ in range(n)]
path = [0] * n
build(max(1, int(log2(n))), 0, 0, 10 ** 20)
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    stdout.write(f'{lca(max(1, int(log2(n))), x, y)}\n')
