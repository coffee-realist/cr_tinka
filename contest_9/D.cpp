#include <cstdio>
#include <vector>
#include <algorithm>
#include <tuple>
#pragma GCC optimize("Ofast")

using namespace std;

const int TREE_SIZE = 524288;
vector<pair<int, int>> segmentTree(TREE_SIZE * 2);
vector<int> lazyValues(TREE_SIZE * 2);

struct Coord {
    int x;
    int lowerY;
    int upperY;
};

bool compareEvent(pair<Coord, int> a, pair<Coord, int> b) {
    return (a.first.x == b.first.x) ? (a.second > b.second) : (a.first.x < b.first.x);
}

pair<int, int> buildSegmentTree(int idx, int left, int right) {
    if (right - left == 1) {
        segmentTree[idx].second = left;
        return segmentTree[idx];
    }
    int middle = (left + right) / 2;
    pair<int, int> leftChild = buildSegmentTree(idx * 2 + 1, left, middle);
    pair<int, int> rightChild = buildSegmentTree(idx * 2 + 2, middle, right);
    segmentTree[idx].second = leftChild.second;
    return segmentTree[idx];
}

void updateLazy(int idx, int left, int right) {
    if (lazyValues[idx]) {
        segmentTree[idx].first += lazyValues[idx];
        if (right - left != 1) {
            lazyValues[idx * 2 + 1] += lazyValues[idx];
            lazyValues[idx * 2 + 2] += lazyValues[idx];
        }
        lazyValues[idx] = 0;
    }
}

pair<int, int> query(int idx, int queryL, int queryR, int left, int right) {
    updateLazy(idx, left, right);
    if (left == queryL && right == queryR) return segmentTree[idx];

    if (left >= queryR || queryL >= right) return {0, queryL};

    int middle = (left + right) / 2;
    pair<int, int> leftResult = query(idx * 2 + 1, queryL, min(queryR, middle), left, middle);
    pair<int, int> rightResult = query(idx * 2 + 2, max(middle, queryL), queryR, middle, right);
    return (leftResult.first < rightResult.first) ? rightResult : leftResult;
}

pair<int, int> update(int idx, int value, int updateL, int updateR, int left, int right) {
    updateLazy(idx, left, right);
    if (left == updateL && right == updateR) {
        lazyValues[idx] = value;
        updateLazy(idx, left, right);
        return segmentTree[idx];
    }
    if (left >= updateR || updateL >= right) return segmentTree[idx];

    int middle = (left + right) / 2;
    pair<int, int> leftUpdate = update(idx * 2 + 1, value, updateL, min(updateR, middle), left, middle);
    pair<int, int> rightUpdate = update(idx * 2 + 2, value, max(middle, updateL), updateR, middle, right);
    segmentTree[idx] = (rightUpdate.first > leftUpdate.first) ? rightUpdate : leftUpdate;
    return segmentTree[idx];
}

int main() {
    buildSegmentTree(0, 0, TREE_SIZE);

    int n;
    scanf("%d", &n);
    vector<pair<Coord, int>> events;
    events.reserve(n * 2);

    const int OFFSET = 200000;
    for (int i = 0; i < n; i++) {
        int x1, lowerY, x2, upperY;
        scanf("%d %d %d %d", &x1, &lowerY, &x2, &upperY);
        Coord startPoint = {x1, lowerY + OFFSET, upperY + OFFSET};
        Coord endPoint = {x2, lowerY + OFFSET, upperY + OFFSET};
        events.push_back({startPoint, 1});
        events.push_back({endPoint, -1});
    }
    sort(events.begin(), events.end(), compareEvent);

    tuple<int, int, int> result;
    for (auto &event : events) {
        update(0, event.second, event.first.lowerY, event.first.upperY + 1, 0, TREE_SIZE);
        pair<int, int> best = query(0, event.first.lowerY, event.first.upperY + 1, 0, TREE_SIZE);
        if (best.first > get<0>(result)) {
            result = make_tuple(best.first, event.first.x, best.second - OFFSET);
        }
    }

    printf("%d\n", get<0>(result));
    printf("%d %d\n", get<1>(result), get<2>(result));
    return 0;
}