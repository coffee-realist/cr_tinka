#include <vector>
#include <algorithm>
#include <stdio.h>
#include <cmath>
#pragma GCC optimize("Ofast")

struct Vertex {
    int v = 0, sectors = 0, l, r;
    bool flag = false, top = false;
    Vertex() {}
    Vertex(int a, int b) {
        l = a;
        r = b;
    }
};


void build(std::vector<Vertex> &tree, int v, int tl, int tr) {
    tree[v] = Vertex(tl, tr);
    if (tl != tr) {
        int tm = (tl + tr) / 2;
        build(tree, v * 2, tl, tm);
        build(tree, v * 2 + 1, tm + 1, tr);
    }
}

void push(std::vector<Vertex> &tree, int v) {
    if (!tree[v].top)
        return;
    tree[v].v = (tree[v].flag ? (tree[v].r - tree[v].l + 1) : 0);
    tree[v].sectors = (tree[v].flag ? 1 : 0);
    tree[v].top = false;
    if (tree[v].l == tree[v].r)
        return;
    tree[v * 2 + 1].flag = tree[v].flag;
    tree[v * 2].flag = tree[v].flag;
    tree[v * 2 + 1].top = true;
    tree[v * 2].top = true;
}

void update(std::vector<Vertex> &tree, int v, int l, int r, bool flag) {
    if (tree[v].r < l || tree[v].l > r)
        return;
    if (tree[v].r <= r && tree[v].l >= l) {
        push(tree, v);
        tree[v].flag = flag;
        tree[v].top = true;
        return;
    }
    push(tree, v);
    update(tree, v * 2, l, r, flag);
    update(tree, v * 2 + 1, l, r, flag);
    int node = v * 2;
    while (true) {
        push(tree, node);
        if (tree[node].l == tree[node].r)
            break;
        node = node * 2 + 1;
    }
    bool left = (tree[node].v == 1);
    node = v * 2 + 1;
    while (true) {
        push(tree, node);
        if (tree[node].l == tree[node].r)
            break;
        node *= 2;
    }
    bool right = tree[node].v == 1;
    tree[v].v = tree[v * 2].v + tree[v * 2 + 1].v;
    tree[v].sectors = tree[v * 2].sectors + tree[v * 2 + 1].sectors;
    if (left && right)
        tree[v].sectors--;
}

int main() {
    int mx_size = 1e6, delta = 5e5, n, x, l;
    char c;
    scanf("%d", &n);
    std::vector<Vertex> tree((1 << ((int)log2(mx_size) + 1)) * 2 - 1);
    build(tree, 1, 0, mx_size);
    for (int _ = 0; _ < n; _++) {
        scanf(" %c %d %d", &c, &x, &l);
        l > 0 ? l--: l++;
        update(tree, 1, x + delta, x + l + delta, c == 'B');
        printf("%d %d\n", tree[1].sectors, tree[1].v);
    }
    return 0;
}