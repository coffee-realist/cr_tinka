#include <stdio.h>
#include <set>
#include <algorithm>
#pragma GCC optimize("Ofast")

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    set<pair<int, int>> cells;
    for (int i = 0; i < n; ++i) {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);

        if (a == c) {
            int min_y = min(b, d);
            int max_y = max(b, d);
            for (int y = min_y; y <= max_y; ++y) {
                cells.emplace(a, y);
            }
        } else {
            int min_x = min(a, c);
            int max_x = max(a, c);
            for (int x = min_x; x <= max_x; ++x) {
                cells.emplace(x, b);
            }
        }
    }
    printf("%d\n", (int)cells.size());
    return 0;
}
