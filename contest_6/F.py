from collections import deque


def shortest_path_length():
    if start == end:
        return 0
    checked = [0] * (cur_id + 1)
    d = deque([(start, 0)])
    while d:
        v, dist = d.popleft()
        checked[v] = 1
        try:
            for u in g[v]:
                if u == end:
                    return dist + 1
                if not checked[u]:
                    d.append((u, dist + 1))
                    checked[u] = 1
        except KeyError:
            pass
    return -1


m = int(input())
g = dict()
result = []
ids = dict()
cur_id = 0
for i in range(m):
    _1, _2 = input().split(' -> ')
    try:
        c = ids[_1]
    except KeyError:
        ids[_1] = cur_id
        cur_id += 1
    try:
        c = ids[_2]
    except KeyError:
        ids[_2] = cur_id
        cur_id += 1
    try:
        g[ids[_1]].append(ids[_2])
    except KeyError:
        g[ids[_1]] = [ids[_2]]
try:
    start = ids[input()]
    end = ids[input()]
    print(shortest_path_length())
except KeyError:
    print(-1)
