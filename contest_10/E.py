import heapq
from sys import maxsize, stdin

input = stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(1, m + 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
dist = [maxsize] * (n + 1)
dist[1] = 0
q = [(0, 1)]
while q:
    cur_dist, u = heapq.heappop(q)
    if cur_dist > dist[u]:
        continue
    for v, weight in graph[u]:
        distance = cur_dist + weight
        if distance < dist[v]:
            dist[v] = distance
            heapq.heappush(q, (distance, v))
print(*dist[1:])
