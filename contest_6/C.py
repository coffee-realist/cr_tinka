from sys import stdin

input = stdin.readline


def is_topological_sort():
    position = {v: pos for pos, v in enumerate(order)}
    for vertex, edges in g.items():
        current_pos = position[vertex]
        for neighbor in edges:
            if position[neighbor] <= current_pos:
                return False
    return True


n, m = map(int, input().split())
g = dict()
result = []
for _ in range(m):
    _1, _2 = map(int, input().split())
    try:
        g[_1].append(_2)
    except KeyError:
        g[_1] = [_2]
order = list(map(int, input().split()))
if is_topological_sort():
    print('YES')
else:
    print('NO')
