from sys import setrecursionlimit

setrecursionlimit(100000)


class SegmentTree:
    def __init__(self, elements):
        self.tree = [0] * (4 * n)
        self.build(elements, 0, 0, n - 1)

    def build(self, arr, x, tl, tr):
        if tl == tr:
            self.tree[x] = arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(arr, x * 2 + 1, tl, tm)
            self.build(arr, x * 2 + 2, tm + 1, tr)
            self.tree[x] = self.tree[x * 2 + 1] + self.tree[x * 2 + 2]

    def sum(self, x, tl, tr, left, right):
        if left > right:
            return 0
        if left == tl and right == tr:
            return self.tree[x]
        tm = (tl + tr) // 2
        return self.sum(x * 2 + 1, tl, tm, left, min(right, tm)) + self.sum(x * 2 + 2, tm + 1, tr, max(left, tm + 1),
                                                                            right)

    def update(self, x, tl, tr, ind, value):
        if tl == tr:
            self.tree[x] = value
        else:
            tm = (tl + tr) // 2
            if ind <= tm:
                self.update(x * 2 + 1, tl, tm, ind, value)
            else:
                self.update(x * 2 + 2, tm + 1, tr, ind, value)
            self.tree[x] = self.tree[x * 2 + 1] + self.tree[x * 2 + 2]


n, m = map(int, input().split())
lst = list(map(int, input().split()))
seg_tree = SegmentTree(lst)
for _ in range(m):
    query, *args = map(int, input().split())
    if query == 1:
        i, v = args
        seg_tree.update(0, 0, n - 1, i, v)
    elif query == 2:
        l, r = args
        print(seg_tree.sum(0, 0, n - 1, l, r - 1))
