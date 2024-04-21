from sys import setrecursionlimit
from math import inf

setrecursionlimit(100000)


class SegmentTree:
    def __init__(self, elements):
        self.tree = [None] * (4 * n)
        self.build(elements, 0, 0, n - 1)

    def build(self, arr, x, tl, tr):
        if tl == tr:
            self.tree[x] = (arr[tl], 1)
        else:
            tm = (tl + tr) // 2
            self.build(arr, x * 2 + 1, tl, tm)
            self.build(arr, x * 2 + 2, tm + 1, tr)
            self.tree[x] = self.merge(self.tree[x * 2 + 1], self.tree[x * 2 + 2])

    @staticmethod
    def merge(left, right):
        if left[0] == right[0]:
            return left[0], left[1] + right[1]
        elif left[0] < right[0]:
            return left
        else:
            return right

    def min(self, x, tl, tr, left, right):
        if left > right:
            return inf, 0
        if left == tl and right == tr:
            return self.tree[x]
        tm = (tl + tr) // 2
        return self.merge(
            self.min(x * 2 + 1, tl, tm, left, min(right, tm)),
            self.min(x * 2 + 2, tm + 1, tr, max(left, tm + 1), right)
        )

    def update(self, x, tl, tr, ind, value):
        if tl == tr:
            self.tree[x] = (value, 1)
        else:
            tm = (tl + tr) // 2
            if ind <= tm:
                self.update(x * 2 + 1, tl, tm, ind, value)
            else:
                self.update(x * 2 + 2, tm + 1, tr, ind, value)
            self.tree[x] = self.merge(self.tree[x * 2 + 1], self.tree[x * 2 + 2])


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
        print(*seg_tree.min(0, 0, n - 1, l, r - 1))
