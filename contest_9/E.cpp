#include <cstdio>
#include <algorithm>
#pragma GCC optimize("Ofast")

using namespace std;

typedef long long ll;
const int MAX_SEGMENTS = 200002;
#define left_child (idx << 1)
#define right_child ((idx << 1) | 1)

struct Interval {
    int start_x, end_x, coord_y, delta;
    bool operator<(const Interval &other) const {
        return coord_y < other.coord_y;
    }
} segments[MAX_SEGMENTS];

int sortedX[MAX_SEGMENTS];
int segmentTree[MAX_SEGMENTS << 2], activeCover[MAX_SEGMENTS << 2];


void updateSegmentTree(int idx, int lBound, int rBound) {
    if (activeCover[idx] > 0) {
        segmentTree[idx] = sortedX[rBound] - sortedX[lBound];
    } else {
        segmentTree[idx] = (lBound + 1 != rBound) ? segmentTree[left_child] + segmentTree[right_child] : 0;
    }
}

void modify(int idx, int lBound, int rBound, int queryL, int queryR, int value) {
    if (queryL <= lBound && rBound <= queryR) {
        activeCover[idx] += value;
    } else {
        int mid = (lBound + rBound) / 2;
        if (queryL < mid) modify(left_child, lBound, mid, queryL, min(mid, queryR), value);
        if (queryR > mid) modify(right_child, mid, rBound, max(mid, queryL), queryR, value);
    }
    updateSegmentTree(idx, lBound, rBound);
}

int main() {
    int n;
    scanf("%d", &n);
    int eventCount = 0;
    for (int i = 0; i < n; ++i) {
        int startX, startY, endX, endY;
        scanf("%d %d %d %d", &startX, &startY, &endX, &endY);
        if (startX > endX || startY > endY) {
            swap(startX, endX), swap(startY, endY);
        }
        startX--, startY--;
        segments[eventCount] = {startX, endX, startY, 1};
        sortedX[eventCount++] = startX;
        segments[eventCount] = {startX, endX, endY, -1};
        sortedX[eventCount++] = endX;
    }
    sort(sortedX, sortedX + eventCount);
    eventCount = unique(sortedX, sortedX + eventCount) - sortedX;
    sort(segments, segments + 2 * n);
    ll result = 0;
    for (int i = 0; i < 2 * n - 1; i++) {
        int leftIdx = lower_bound(sortedX, sortedX + eventCount, segments[i].start_x) - sortedX;
        int rightIdx = lower_bound(sortedX, sortedX + eventCount, segments[i].end_x) - sortedX;
        modify(1, 0, eventCount - 1, leftIdx, rightIdx, segments[i].delta);
        result += (ll)segmentTree[1] * (segments[i + 1].coord_y - segments[i].coord_y);
    }
    printf("%lld\n", result);
    return 0;
}
