from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(1000000000)


def dfs(v):
    global conditions
    conditions[v] = 1
    for u in g[v]:
        if conditions[u] == 0:
            dfs(u)
        if conditions[u] == 1:
            return 1
    conditions[v] = 2
    return 0


n, m = map(int, input().split())
g = [[] for _ in range(n)]
conditions = [0] * n
for _ in range(m):
    _1, _2 = map(int, input().split())
    g[_1 - 1].append(_2 - 1)
print(dfs(_1 - 1))
