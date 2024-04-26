from sys import stdin, stdout


class DSU:
    def __init__(self):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.min = list(range(n))
        self.max = list(range(n))
        self.size = [1] * n

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
                self.min[root_a] = min(self.min[root_a], self.min[root_b])
                self.max[root_a] = max(self.max[root_a], self.max[root_b])
                self.size[root_a] += self.size[root_b]
            elif self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
                self.min[root_b] = min(self.min[root_a], self.min[root_b])
                self.max[root_b] = max(self.max[root_a], self.max[root_b])
                self.size[root_b] += self.size[root_a]
            else:
                self.parent[root_b] = root_a
                self.min[root_a] = min(self.min[root_a], self.min[root_b])
                self.max[root_a] = max(self.max[root_a], self.max[root_b])
                self.size[root_a] += self.size[root_b]
                self.rank[root_a] += 1

    def get(self, a):
        root = self.find(a)
        return self.min[root] + 1, self.max[root] + 1, self.size[root]


input = stdin.readline
n, m = map(int, input().split())
dsu = DSU()
for _ in range(m):
    op = input().split()
    if op[0] == "union":
        x, y = map(int, op[1:])
        dsu.union(x - 1, y - 1)
    elif op[0] == "get":
        x = int(op[1])
        mn, mx, cnt = dsu.get(x - 1)
        stdout.write(f'{mn} {mx} {cnt}\n')
