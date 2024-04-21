from sys import maxsize, setrecursionlimit, stdin, stdout

setrecursionlimit(10 ** 5)
input = stdin.readline


class SegmentTree:
    def __init__(self):
        self.tree = [[0, 0] for _ in range((1 << (n - 1).bit_length()) * 2 - 1)]

    def get_min(self, v, tl, tr, l, r):
        if l > r:
            return maxsize
        if l == tl and tr == r:
            return self.tree[v][0] + self.tree[v][1]
        tm = (tl + tr) // 2
        return min(
            self.get_min(v * 2, tl, tm, l, min(r, tm)),
            self.get_min(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
        ) + self.tree[v][1]

    def update(self, v, tl, tr, l, r, x):
        if l > r:
            return
        if l == tl and tr == r:
            self.tree[v][1] += x
        else:
            tm = (tl + tr) // 2
            self.update(v * 2, tl, tm, l, min(r, tm), x)
            self.update(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, x)
            self.tree[v][0] = min(
                self.tree[v * 2][0] + self.tree[v * 2][1],
                self.tree[v * 2 + 1][0] + self.tree[v * 2 + 1][1]
            )


n, m = map(int, input().split())
st = SegmentTree()
for _ in range(m):
    q, *args = map(int, input().split())
    if q == 1:
        l, r, v = args
        st.update(1, 0, n - 1, l, r - 1, v)
    else:
        l, r = args
        stdout.write(f'{st.get_min(1, 0, n - 1, l, r - 1)}\n')
'''
5 6
1 0 3 3
2 1 2
1 1 4 4
2 1 3
2 1 4
2 3 5

'''
