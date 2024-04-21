#include <vector>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#pragma GCC optimize("Ofast")

struct Vertex {
    long long s, delta;
    int flag;
    Vertex() {
        s = 0;
        delta = 0;
        flag = -1;
    }
};

void push(std::vector<Vertex> &tree, int v, int len) {
    if (tree[v].flag != -1) {
        if (len != 1) {
            tree[v * 2 + 1].flag = tree[v].flag;
            tree[v * 2].flag = tree[v * 2 + 1].flag;
            tree[v * 2 + 1].delta = 0;
            tree[v * 2].delta = 0;
        }
        tree[v].s = (long long)tree[v].flag * len;
    }
    tree[v].flag = -1;
    if (len != 1) {
        tree[v * 2].delta += tree[v].delta;
        tree[v * 2 + 1].delta += tree[v].delta;
    }
    tree[v].s += tree[v].delta * len;
    tree[v].delta = 0;
}

long long sum(std::vector<Vertex> &tree, int v, int tl, int tr, int l, int r) {
    push(tree, v, tr - tl + 1);
    if (l > r)
        return 0;
    if (l == tl && tr == r)
        return tree[v].s;
    int tm = (tl + tr) / 2;
    return sum(tree, v * 2, tl, tm, l, std::min(r, tm)) + sum(tree, v * 2 + 1, tm + 1, tr, std::max(l, tm + 1), r);
}

void update(std::vector<Vertex> &tree, int v, int tl, int tr, int l, int r, int x) {
    push(tree, v, tr - tl + 1);
    if (l > r)
        return;
    if (l == tl && tr == r) {
        tree[v].flag = x;
        tree[v].delta = 0;
        push(tree, v, tr - tl + 1);
    }
    else {
        int tm = (tl + tr) / 2;
        update(tree, v * 2, tl, tm, l, std::min(r, tm), x);
        update(tree, v * 2 + 1, tm + 1, tr, std::max(l, tm + 1), r, x);
        tree[v].s = tree[v * 2].s + tree[v * 2 + 1].s;
    }
}

void add(std::vector<Vertex> &tree, int v, int tl, int tr, int l, int r, int x) {
    push(tree, v, tr - tl + 1);
    if (l > r)
        return;
    if (l == tl && tr == r) {
        tree[v].delta += x;
        push(tree, v, tr - tl + 1);
    }
    else {
        int tm = (tl + tr) / 2;
        add(tree, v * 2, tl, tm, l, std::min(r, tm), x);
        add(tree, v * 2 + 1, tm + 1, tr, std::max(l, tm + 1), r, x);
        tree[v].s = tree[v * 2].s + tree[v * 2 + 1].s;
    }
}


int main() {
    int n, m, q, l, r, v;
    scanf("%d %d", &n, &m);
    std::vector<Vertex> tree((1 << ((int)log2(n) + 1)) * 2 - 1);
    for (int _ = 0; _ < m; _++) {
        scanf("%d", &q);
        if (q == 1) {
            scanf("%d %d %d", &l, &r, &v);
            update(tree, 1, 0, n - 1, l, r - 1, v);
        }
        else if (q == 2) {
            scanf("%d %d %d", &l, &r, &v);
            add(tree, 1, 0, n - 1, l, r - 1, v);

        }
        else {
            scanf("%d %d", &l, &r);
            printf("%lld\n", sum(tree, 1, 0, n - 1, l, r - 1));
        }
    }
}