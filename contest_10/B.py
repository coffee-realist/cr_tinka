from sys import stdin


class DSU:
    def __init__(self):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            elif self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            else:
                self.parent[root_b] = root_a
                self.rank[root_a] += 1


input = stdin.readline
n, m = map(int, input().split())
dsu = DSU()
mst_weight = 0
edge_count = 0
for u, v, w in sorted([list(map(int, input().split())) for _ in range(m)], key=lambda edge: edge[2]):
    if dsu.find(u - 1) != dsu.find(v - 1):
        dsu.union(u - 1, v - 1)
        mst_weight += w
        edge_count += 1
        if edge_count == n - 1:
            break
print(mst_weight)
