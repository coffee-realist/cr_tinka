from sys import setrecursionlimit

setrecursionlimit(100000)


class SegmentTree:
    def __init__(self, elements):
        self.tree_size = 1 << (n - 1).bit_length()
        self.tree = [0] * (2 * self.tree_size - 1)
        self.build(elements, 0, 0, n - 1)

    def build(self, arr, v, tl, tr):
        if tl == tr:
            self.tree[v] = arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(arr, v * 2 + 1, tl, tm)
            self.build(arr, v * 2 + 2, tm + 1, tr)
            self.tree[v] = self.tree[v * 2 + 1] + self.tree[v * 2 + 2]

    def update(self, v, tl, tr, ind):
        if tl == tr:
            self.tree[v] = 1 - self.tree[v]
        else:
            tm = (tl + tr) // 2
            if ind <= tm:
                self.update(v * 2 + 1, tl, tm, ind)
            else:
                self.update(v * 2 + 2, tm + 1, tr, ind)
            self.tree[v] = self.tree[v * 2 + 1] + self.tree[v * 2 + 2]

    def kth_one(self, v, tl, tr, k):
        if tl == tr:
            return tl
        tm = (tl + tr) // 2
        left_child = self.tree[v * 2 + 1]
        if k < left_child:
            return self.kth_one(v * 2 + 1, tl, tm, k)
        else:
            return self.kth_one(v * 2 + 2, tm + 1, tr, k - left_child)


n, m = map(int, input().split())
lst = list(map(int, input().split()))
seg_tree = SegmentTree(lst)
for _ in range(m):
    query, arg = map(int, input().split())
    if query == 1:
        seg_tree.update(0, 0, n - 1, arg)
    elif query == 2:
        print(seg_tree.kth_one(0, 0, n - 1, arg))
