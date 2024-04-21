from sys import setrecursionlimit, stdin, stdout

setrecursionlimit(2 * 10 ** 4)
input = stdin.readline


class Node:
    def __init__(self, l, r):
        self.left = l
        self.right = r
        self.cnt = 0
        self.v = 0
        self.flag = False
        self.up = False


class SegmentTree:
    def __init__(self):
        self.tree = [None] * (4 * (10 ** 6 + 10 ** 2))
        self.build(1, 0, 10 ** 6 + 10 ** 2)

    def build(self, v, tl, tr):
        self.tree[v] = Node(tl, tr)
        if tl != tr:
            tm = (tl + tr) // 2
            self.build(v * 2, tl, tm)
            self.build(v * 2 + 1, tm + 1, tr)

    def push(self, v):
        if not self.tree[v].up:
            return
        self.tree[v].v = (self.tree[v].flag * (self.tree[v].right - self.tree[v].left + 1)) if self.tree[
            v].flag else 0
        self.tree[v].cnt = 1 if self.tree[v].flag else 0
        self.tree[v].up = False
        if self.tree[v].left == self.tree[v].right:
            return
        self.tree[v * 2].flag = self.tree[v * 2 + 1].flag = self.tree[v].flag
        self.tree[v * 2].up = self.tree[v * 2 + 1].up = True

    def update(self, v, value, l, r):
        if self.tree[v].right < l or self.tree[v].left > r:
            return
        if self.tree[v].right <= r and self.tree[v].left >= l:
            self.push(v)
            self.tree[v].flag = value
            self.tree[v].up = True
            return
        self.push(v)
        self.update(v * 2, value, l, r)
        self.update(v * 2 + 1, value, l, r)
        cur = v * 2
        while True:
            self.push(cur)
            if self.tree[cur].left == self.tree[cur].right:
                break
            cur = cur * 2 + 1
        left = (self.tree[cur].v == 1)
        cur = v * 2 + 1
        while True:
            self.push(cur)
            if self.tree[cur].left == self.tree[cur].right:
                break
            cur = cur * 2
        right = (self.tree[cur].v == 1)
        self.tree[v].v = self.tree[v * 2].v + self.tree[v * 2 + 1].v
        self.tree[v].cnt = self.tree[v * 2].cnt + self.tree[v * 2 + 1].cnt
        if left and right:
            self.tree[v].cnt -= 1


n = int(input())
st = SegmentTree()
d = 5 * 10 ** 5
for _ in range(n):
    c, x, l = input().split()
    x, l = int(x), int(l)
    if l > 0:
        l -= 1
    else:
        l += 1
    st.update(1, c == 'B', x + d, x + l + d)
    stdout.write(f'{st.tree[1].cnt} {st.tree[1].v}\n')

'''
7
W 2 3
B 2 2
B 4 2
B 3 2
B 7 2
W 3 1
W 0 10

'''
