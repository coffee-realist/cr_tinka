#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>
#pragma GCC optimize("Ofast")

using namespace std;

struct Point {
    long long coordX, coordY;
    int pointId;
};

void readInput(int& totalPoints, vector<Point>& points, vector<long long>& heights) {
    scanf("%*d %*d %d", &totalPoints);
    points.resize(totalPoints);
    double inputX, inputY;
    for (int i = 0; i < totalPoints; i++) {
        scanf("%lf %lf", &inputX, &inputY);
        points[i] = Point{(long long)(inputX * 2), (long long)(inputY * 2), i};
    }
    heights.resize(totalPoints);
    for (int i = 0; i < totalPoints; i++)
        heights[i] = points[i].coordY;
}

long long getPrefixSum(vector<long long>& sumVector, int idx) {
    long long total = 0;
    for (; idx >= 0; idx = (idx & (idx + 1)) - 1)
        total += sumVector[idx];
    return total;
}

void updateBIT(vector<long long>& sumVector, int idx, long long value) {
    for (; idx < (int)sumVector.size(); idx = idx | (idx + 1))
        sumVector[idx] += value;
}

void processPoints(vector<Point>& points, vector<long long>& rank, vector<long long>& output) {
    sort(rank.begin(), rank.end());
    rank.erase(unique(rank.begin(), rank.end()), rank.end());
    sort(points.begin(), points.end(), [](const Point& a, const Point& b) {
        return a.coordX < b.coordX;
    });
    vector<long long> prefixSum(rank.size(), 0);
    for (Point& pt : points) {
        auto itY = lower_bound(rank.begin(), rank.end(), pt.coordY);
        int yPos = int(itY - rank.begin());
        long long dist = pt.coordX - getPrefixSum(prefixSum, yPos);
        output[pt.pointId] = dist;
        auto itLow = upper_bound(rank.begin(), rank.end(), pt.coordY - dist);
        auto itHigh = upper_bound(rank.begin(), rank.end(), pt.coordY + dist);
        int posYLow = int(itLow - rank.begin());
        int posYHigh = int(itHigh - rank.begin());
        updateBIT(prefixSum, posYLow, dist * 2);
        updateBIT(prefixSum, posYHigh, -dist * 2);
    }
}

int main() {
    int numPoints;
    vector<Point> points;
    vector<long long> heights;
    readInput(numPoints, points, heights);
    vector<long long> distances(numPoints, 0);
    processPoints(points, heights, distances);
    for (long long distance : distances)
        printf("%lld ", distance);
    return 0;
}
