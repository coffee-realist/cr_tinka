from sys import setrecursionlimit, stdin, stdout

setrecursionlimit(5 * 10 ** 4)
input = stdin.readline


class Node:
    def __init__(self):
        self.sum = 0
        self.delta = 0
        self.replace = -1


class SegmentTree:
    def __init__(self):
        self.tree = [Node() for _ in range(n * 4)]

    def push(self, v, tree_size):
        if self.tree[v].replace != -1:
            if tree_size != 1:
                self.tree[v * 2].replace = self.tree[v * 2 + 1].replace = self.tree[v].replace
                self.tree[v * 2].delta = self.tree[v * 2 + 1].delta = 0
            self.tree[v].sum = self.tree[v].replace * tree_size
        self.tree[v].replace = -1
        if tree_size != 1:
            self.tree[v * 2].delta += self.tree[v].delta
            self.tree[v * 2 + 1].delta += self.tree[v].delta
        self.tree[v].sum += self.tree[v].delta * tree_size
        self.tree[v].delta = 0

    def sum(self, v, tl, tr, l, r):
        self.push(v, tr - tl + 1)
        if l > r:
            return 0
        if l == tl and tr == r:
            return self.tree[v].sum
        tm = (tl + tr) // 2
        return self.sum(v * 2, tl, tm, l, min(r, tm)) + self.sum(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)

    def change(self, v, tl, tr, l, r, x):
        self.push(v, tr - tl + 1)
        if l > r:
            return
        if l == tl and tr == r:
            self.tree[v].replace = x
            self.tree[v].delta = 0
            self.push(v, tr - tl + 1)
        else:
            tm = (tl + tr) // 2
            self.change(v * 2, tl, tm, l, min(r, tm), x)
            self.change(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, x)
            self.tree[v].sum = self.tree[v * 2].sum + self.tree[v * 2 + 1].sum

    def add(self, v, tl, tr, l, r, x):
        self.push(v, tr - tl + 1)
        if l > r:
            return
        if l == tl and tr == r:
            self.tree[v].delta += x
            self.push(v, tr - tl + 1)
        else:
            tm = (tl + tr) // 2
            self.add(v * 2, tl, tm, l, min(r, tm), x)
            self.add(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, x)
            self.tree[v].sum = self.tree[v * 2].sum + self.tree[v * 2 + 1].sum


n, m = map(int, input().split())
st = SegmentTree()
for _ in range(m):
    q, *args = map(int, input().split())
    if q == 1:
        l, r, v = args
        st.change(1, 0, n - 1, l, r - 1, v)
    elif q == 2:
        l, r, v = args
        st.add(1, 0, n - 1, l, r - 1, v)
    else:
        l, r = args
        stdout.write(f'{st.sum(1, 0, n - 1, l, r - 1)}\n')

'''
5 7
1 0 3 3
2 2 4 2
3 1 3
2 1 5 1
1 0 2 2
3 0 3
3 3 5

'''
