#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#pragma GCC optimize("Ofast")

using namespace std;

struct LineSegment {
    int altitude, segment_start, segment_end;
    bool start;

    LineSegment(int alt = 0, int start_ = 0, int end_ = 0, bool st = false) :
        altitude(alt), segment_start(start_), segment_end(end_), start(st) {}
};

bool compLines(const LineSegment &a, const LineSegment &b) {
    if (a.altitude == b.altitude) return a.start && !b.start;
    return a.altitude < b.altitude;
}

struct SegmentTree {
    vector<int> tree, lazy;
    int size;

    SegmentTree(int sz) : size(sz), tree(4 * sz, 0), lazy(4 * sz, 0) {}

    void propagate(int idx, int l, int r) {
        if (lazy[idx] != 0) {
            tree[idx] += lazy[idx];
            if (l != r) {
                lazy[idx * 2 + 1] += lazy[idx];
                lazy[idx * 2 + 2] += lazy[idx];
            }
            lazy[idx] = 0;
        }
    }

    void update(int idx, int l, int r, int start, int end, int val) {
        propagate(idx, l, r);
        if (l > end || r < start) return;
        if (l >= start && r <= end) {
            lazy[idx] += val;
            propagate(idx, l, r);
            return;
        }
        int mid = (l + r) / 2;
        update(idx * 2 + 1, l, mid, start, end, val);
        update(idx * 2 + 2, mid + 1, r, start, end, val);
        tree[idx] = max(tree[idx * 2 + 1], tree[idx * 2 + 2]);
    }

    int getMax() {
        propagate(0, 0, size - 1);
        return tree[0];
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    vector<LineSegment> events;
    int OFFSET = 200000;

    for (int i = 0; i < n; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        x1 += OFFSET; x2 += OFFSET;
        y1 += OFFSET; y2 += OFFSET;
        events.push_back(LineSegment(y1, x1, x2, true));
        events.push_back(LineSegment(y2, x1, x2, false));
    }

    sort(events.begin(), events.end(), compLines);

    int TREE_SIZE = 1;
    while (TREE_SIZE <= 2 * OFFSET) TREE_SIZE <<= 1;

    SegmentTree segTree(TREE_SIZE);
    int maxCoverage = 0, maxX = -1, maxY = -1;

    for (auto &e : events) {
        int val = (e.start ? 1 : -1);
        segTree.update(0, 0, TREE_SIZE - 1, e.segment_start, e.segment_end, val);
        int currentMax = segTree.getMax();
        if (currentMax > maxCoverage) {
            maxCoverage = currentMax;
            maxX = e.segment_start - OFFSET;
            maxY = e.altitude - OFFSET;
        }
    }

    cout << maxCoverage << endl << maxX << ' ' << maxY << endl;
    return 0;
}
