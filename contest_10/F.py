from sys import stdin, maxsize
import heapq


def f(cnt):
    dist = [maxsize] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        current_time, u = heapq.heappop(pq)
        if current_time > dist[u]:
            continue
        for v, t, mx_w in graph[u]:
            if mx_w >= int(3e6) + cnt * 100 and dist[v] > current_time + t:
                dist[v] = current_time + t
                heapq.heappush(pq, (dist[v], v))
    return dist[n] <= 1440


input = stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, t, w = map(int, input().split())
    graph[u].append((v, t, w))
    graph[v].append((u, t, w))
left, right = 0, 10 ** 7
result = 0
while left <= right:
    mid = (left + right) // 2
    if f(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)