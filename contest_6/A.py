from sys import stdin

input = stdin.readline


def get_connectivity_components_cnt():
    i = 0
    visited = [0] * n
    result = []
    for cur in range(n):
        if visited[cur]:
            continue
        visited[cur] = 1
        lst = [cur]
        result.append([])
        while lst:
            v = lst.pop()
            result[i].append(v + 1)
            for u in g[v]:
                if not visited[u]:
                    visited[u] = 1
                    lst.append(u)
        i += 1
    return result


n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    _1, _2 = map(int, input().split())
    g[_1 - 1].append(_2 - 1)
    g[_2 - 1].append(_1 - 1)
components = get_connectivity_components_cnt()
print(len(components))
for component in components:
    print(len(component))
    print(*sorted(component))
