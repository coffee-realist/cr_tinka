#include <algorithm>
#include <climits>
#include <stdio.h>
#include <vector>
#include <cmath>

class SegmentTree {
public:
    SegmentTree(int size) {
        int n = 1 << ((int)log2(size) + 1);
        tree.resize(2 * n - 1, std::vector<long long>(2, 0));
    }

    long long getMin(int v, int tl, int tr, int l, int r) {
        if (l > r) {
            return LLONG_MAX;
        }
        if (l == tl && tr == r) {
            return tree[v][0] + tree[v][1];
        }
        int tm = (tl + tr) / 2;
        return std::min(
            getMin(v * 2, tl, tm, l, std::min(r, tm)),
            getMin(v * 2 + 1, tm + 1, tr, std::max(l, tm + 1), r)
        ) + tree[v][1];
    }

    void update(int v, int tl, int tr, int l, int r, long long x) {
        if (l > r) {
            return;
        }
        if (l == tl && tr == r) {
            tree[v][1] += x;
        } else {
            int tm = (tl + tr) / 2;
            update(v * 2, tl, tm, l, std::min(r, tm), x);
            update(v * 2 + 1, tm + 1, tr, std::max(l, tm + 1), r, x);
            tree[v][0] = std::min(
                tree[v * 2][0] + tree[v * 2][1],
                tree[v * 2 + 1][0] + tree[v * 2 + 1][1]
            );
        }
    }

private:
    std::vector<std::vector<long long>> tree;
};

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    SegmentTree st(n);
    for (int i = 0; i < m; i++) {
        int q, l, r;
        long long v;
        scanf("%d", &q);
        if (q == 1) {
            scanf("%d %d %lld", &l, &r, &v);
            st.update(1, 0, n - 1, l, r - 1, v);
        } else {
            scanf("%d %d", &l, &r);
            printf("%lld\n", st.getMin(1, 0, n - 1, l, r - 1));
        }
    }
    return 0;
}
