#include <stdio.h>
#include <vector>
#include <algorithm>
#pragma GCC optimize("Ofast")

using namespace std;

int main() {
    int res = 0;
    int n;
    scanf("%d", &n);
    const int seconds_per_day = 60 * 60 * 24;
    vector<int> seconds(seconds_per_day, 0);
    for (int _ = 0; _ < n; _++) {
        int opened_h, opened_m, opened_s, closed_h, closed_m, closed_s;
        scanf("%d %d %d %d %d %d", &opened_h, &opened_m, &opened_s, &closed_h, &closed_m, &closed_s);
        int opened = (opened_h * 60 + opened_m) * 60 + opened_s;
        int closed = (closed_h * 60 + closed_m) * 60 + closed_s;
        if (opened < closed) {
            for (int i = opened; i < closed; ++i) {
                seconds[i] += 1;
            }
        } else {
            for (int i = opened; i < seconds_per_day; ++i) {
                seconds[i] += 1;
            }
            for (int i = 0; i < closed; ++i) {
                seconds[i] += 1;
            }
        }
    }
    res = count(seconds.begin(), seconds.end(), n);
    printf("%d\n", res);
    return 0;
}


