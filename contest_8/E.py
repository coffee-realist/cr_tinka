MOD = 10 ** 9 + 7


class SegmentTree:
    def __init__(self):
        self.tree = []
        self.build_and_solve()

    @staticmethod
    def compress():
        return {value: i + 1 for i, value in enumerate(sorted(set(lst)))}

    def update(self, mx, idx, size, cnt):
        while idx <= mx:
            if size > self.tree[idx][0]:
                self.tree[idx] = (size, cnt)
            elif size == self.tree[idx][0]:
                self.tree[idx] = (self.tree[idx][0], (self.tree[idx][1] + cnt) % MOD)
            idx += idx & -idx

    def query(self, idx):
        mx_size = 0
        mx_cnt = 0
        while idx > 0:
            if self.tree[idx][0] > mx_size:
                mx_size = self.tree[idx][0]
                mx_cnt = self.tree[idx][1]
            elif self.tree[idx][0] == mx_size:
                mx_cnt = (mx_cnt + self.tree[idx][1]) % MOD
            idx -= idx & -idx
        return mx_size, mx_cnt

    def build_and_solve(self):
        if not lst:
            return 0
        compressed = self.compress()
        mx = max(compressed.values())
        self.tree = [(0, 0)] * (mx + 1)
        for value in lst:
            idx = compressed[value]
            mx_size, mx_cnt = self.query(idx - 1)
            self.update(mx, idx, mx_size + 1, mx_cnt if mx_cnt > 0 else 1)
        return self.query(mx)[1]


n = int(input())
lst = list(map(int, input().split()))
st = SegmentTree()
print(st.build_and_solve())
