from sys import setrecursionlimit, maxsize, stdin, stdout

setrecursionlimit(10 ** 7)
input = stdin.readline


class SegmentTree:
    def __init__(self):
        self.tree = [0] * ((1 << (n - 1).bit_length()) * 2 - 1)
        self.build(1, 0, n - 1)

    def build(self, v, tl, tr):
        if tl == tr:
            self.tree[v] = lst[tl]
        else:
            tm = (tl + tr) // 2
            self.build(v * 2, tl, tm)
            self.build(v * 2 + 1, tm + 1, tr)
            self.tree[v] = max(self.tree[v * 2], self.tree[v * 2 + 1])

    def query(self, v, tl, tr, l, r, x):
        if l > r:
            return maxsize
        if tl == tr:
            return tl if self.tree[v] >= x else maxsize
        tm = (tl + tr) // 2
        if tl < l:
            return min(
                self.query(v * 2, tl, tm, l, min(r, tm), x),
                self.query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, x)
            )
        if self.tree[v * 2] >= x:
            return self.query(v * 2, tl, tm, l, min(r, tm), x)
        else:
            return self.query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, x)

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(v * 2, tl, tm, pos, new_val)
            else:
                self.update(v * 2 + 1, tm + 1, tr, pos, new_val)
            self.tree[v] = max(self.tree[v * 2], self.tree[v * 2 + 1])


n, m = map(int, input().split())
lst = list(map(int, input().split()))
st = SegmentTree()
for _ in range(m):
    req_type, *args = map(int, input().split())
    if req_type == 1:
        st.update(1, 0, n - 1, *args)
    else:
        x, lim = args
        res = st.query(1, 0, n - 1, lim, n - 1, x)
        stdout.write(str(-1 if res == maxsize else res) + "\n")

'''
5 7
1 3 2 4 3
2 3 0
2 3 2
1 2 5
2 4 1
2 5 4
1 3 7
2 6 1

'''
