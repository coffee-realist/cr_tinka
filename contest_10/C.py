from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 5)


class DSU:
    def __init__(self):
        self.parent = [i for i in range(n * m)]
        self.rank = [0] * (n * m)

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root != b_root:
            if self.rank[a_root] < self.rank[b_root]:
                self.parent[a_root] = b_root
            elif self.rank[a_root] > self.rank[b_root]:
                self.parent[b_root] = a_root
            else:
                self.parent[b_root] = a_root
                self.rank[a_root] += 1


input = stdin.readline
n, m = map(int, input().split())
edges = []
matrix = [list(map(int, input().split())) for _ in range(n)]
dsu = DSU()
for i in range(n):
    for j in range(m):
        cur = matrix[i][j]
        if j < m - 1:
            if cur & 2:
                dsu.union(i * m + j, i * m + (j + 1))
            else:
                edges.append((2, i * m + j, i * m + (j + 1), 2))
        if i < n - 1:
            if cur & 1:
                dsu.union(i * m + j, (i + 1) * m + j)
            else:
                edges.append((1, i * m + j, (i + 1) * m + j, 1))
edges.sort()
new = []
result = 0
for w, u, v, direction in edges:
    if dsu.find(u) != dsu.find(v):
        dsu.union(u, v)
        new.append((u // m, u % m, direction))
        result += w
stdout.write(f'{len(new)} {result}\n')
for x, y, d in new:
    stdout.write(f'{x + 1} {y + 1} {d}\n')
