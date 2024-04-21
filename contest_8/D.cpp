#include <vector>
#include <climits>
#include <cmath>
#include <stdio.h>
#pragma GCC optimize("Ofast")

using namespace std;

vector<int> lst;

class SegmentTree {
private:
    vector<int> tree;
    int n;

    void build(int v, int tl, int tr) {
        if (tl == tr) {
            tree[v] = lst[tl];
        } else {
            int tm = (tl + tr) / 2;
            build(v * 2, tl, tm);
            build(v * 2 + 1, tm + 1, tr);
            tree[v] = max(tree[v * 2], tree[v * 2 + 1]);
        }
    }

    int query(int v, int tl, int tr, int l, int r, int x) {
        if (l > r) {
            return INT_MAX;
        }
        if (tl == tr) {
            return (tree[v] >= x) ? tl : INT_MAX;
        }
        int tm = (tl + tr) / 2;
        if (tl < l) {
            return min(
                query(v * 2, tl, tm, l, min(r, tm), x),
                query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, x)
            );
        }
        if (tree[v * 2] >= x) {
            return query(v * 2, tl, tm, l, min(r, tm), x);
        } else {
            return query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, x);
        }
    }

    void update(int v, int tl, int tr, int pos, int new_val) {
        if (tl == tr) {
            tree[v] = new_val;
        } else {
            int tm = (tl + tr) / 2;
            if (pos <= tm) {
                update(v * 2, tl, tm, pos, new_val);
            } else {
                update(v * 2 + 1, tm + 1, tr, pos, new_val);
            }
            tree[v] = max(tree[v * 2], tree[v * 2 + 1]);
        }
    }

public:
    SegmentTree(int n_) : n(n_) {
        tree.resize((1 << ((int)log2(n) + 1)) * 2 - 1, 0);
        build(1, 0, n - 1);
    }

    int query(int l, int r, int x) {
        return query(1, 0, n - 1, l, r, x);
    }

    void update(int pos, int new_val) {
        update(1, 0, n - 1, pos, new_val);
    }
};

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    lst.resize(n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &lst[i]);
    }

    SegmentTree st(n);

    for (int i = 0; i < m; i++) {
        int req_type;
        scanf("%d", &req_type);
        if (req_type == 1) {
            int pos, new_val;
            scanf("%d %d", &pos, &new_val);
            st.update(pos, new_val);
        } else {
            int x, lim;
            scanf("%d %d", &x, &lim);
            int res = st.query(lim, n - 1, x);
            printf("%d\n", (res == INT_MAX) ? -1 : res);
        }
    }

    return 0;
}

