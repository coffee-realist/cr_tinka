import heapq
from sys import stdin
from math import inf


def dijkstra(st):
    dist = [inf] * (n + 1)
    dist[st] = 0
    q = [(0, st)]
    while q:
        cur_dist, v = heapq.heappop(q)
        if cur_dist > dist[v]:
            continue
        for u, w in graph[v]:
            d = cur_dist + w
            if d < dist[u]:
                dist[u] = d
                heapq.heappush(q, (d, u))
    return dist


input = stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for u, v, w in [tuple(map(int, input().split())) for _ in range(m)]:
    graph[u].append((v, w))
    graph[v].append((u, w))
a, b, c = map(int, input().split())
dist_a, dist_b, dist_c = dijkstra(a), dijkstra(b), dijkstra(c)
if dist_a[b] == inf or dist_a[c] == inf or dist_b[c] == inf:
    print(-1)
else:
    min_cost = min(
        dist_a[b] + dist_b[c],
        dist_a[c] + dist_c[b],
        dist_b[a] + dist_a[c],
        dist_b[c] + dist_c[a],
        dist_c[a] + dist_a[b],
        dist_c[b] + dist_b[a]
    )
    print(min_cost)
