#include <vector>
#include <climits>
#include <stdio.h>
#pragma GCC optimize("Ofast")

using namespace std;

class SegmentTree {
private:
    vector<pair<int, int>> tree;
    int n;

    pair<int, int> merge(const pair<int, int>& left, const pair<int, int>& right) {
        if (left.first == right.first) {
            return {left.first, left.second + right.second};
        } else if (left.first < right.first) {
            return left;
        } else {
            return right;
        }
    }

    void build(const vector<int>& arr, int x, int tl, int tr) {
        if (tl == tr) {
            tree[x] = {arr[tl], 1};
        } else {
            int tm = (tl + tr) / 2;
            build(arr, x * 2 + 1, tl, tm);
            build(arr, x * 2 + 2, tm + 1, tr);
            tree[x] = merge(tree[x * 2 + 1], tree[x * 2 + 2]);
        }
    }

    pair<int, int> min_cnt(int x, int tl, int tr, int left, int right) {
        if (left > right) {
            return {INT_MAX, 0};
        }
        if (left == tl && right == tr) {
            return tree[x];
        }
        int tm = (tl + tr) / 2;
        return merge(
            min_cnt(x * 2 + 1, tl, tm, left, min(right, tm)),
            min_cnt(x * 2 + 2, tm + 1, tr, max(left, tm + 1), right)
        );
    }

    void update(int x, int tl, int tr, int ind, int value) {
        if (tl == tr) {
            tree[x] = {value, 1};
        } else {
            int tm = (tl + tr) / 2;
            if (ind <= tm) {
                update(x * 2 + 1, tl, tm, ind, value);
            } else {
                update(x * 2 + 2, tm + 1, tr, ind, value);
            }
            tree[x] = merge(tree[x * 2 + 1], tree[x * 2 + 2]);
        }
    }

public:
    SegmentTree(const vector<int>& elements) {
        n = elements.size();
        tree.resize(4 * n, {0, 0});
        build(elements, 0, 0, n - 1);
    }

    pair<int, int> getMin(int left, int right) {
        return min_cnt(0, 0, n - 1, left, right - 1);
    }

    void updateElement(int index, int value) {
        update(0, 0, n - 1, index, value);
    }
};

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> lst(n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &lst[i]);
    }

    SegmentTree seg_tree(lst);

    for (int i = 0; i < m; i++) {
        int query;
        scanf("%d", &query);
        if (query == 1) {
            int index, value;
            scanf("%d %d", &index, &value);
            seg_tree.updateElement(index, value);
        } else if (query == 2) {
            int left, right;
            scanf("%d %d", &left, &right);
            auto result = seg_tree.getMin(left, right);
            printf("%d %d\n", result.first, result.second);
        }
    }

    return 0;
}

