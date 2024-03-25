from math import inf


def floyd(graph):
    d = [[inf] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for u in range(n):
        for v, w in graph[u]:
            d[u][v] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    _1, _2, w_12 = map(int, input().split())
    g[_1 - 1].append([_2 - 1, w_12])
    g[_2 - 1].append([_1 - 1, w_12])
dist = floyd(g)
mid_dist = inf
best_city = -1
for city in range(len(g)):
    max_dist = max(dist[city])
    if max_dist < mid_dist:
        mid_dist = max_dist
        best_city = city
print(best_city + 1)

'''
3 2
1 2 1
2 3 2

6 6
1 3 1
2 4 4
2 5 2
3 4 1
4 6 6
5 6 4

'''
