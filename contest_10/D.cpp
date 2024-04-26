#include <cstdio>
#include <vector>
#include <set>
#include <climits>
#pragma GCC optimize("Ofast")

int main() {
    int n;
    scanf("%d", &n);
    std::vector<int> elements(n + 2), limits(n + 2, INT_MAX);
    for (int i = 1; i <= n; i++)
        scanf("%d", &elements[i]);
    for (int i = 1; i <= n; i++)
        scanf("%d", &limits[i]);
    std::set<int> ind, curs;
    for (int i = 0; i < n + 2; i++) {
        ind.insert(i);
        curs.insert(i);
    }
    for (int i = 0; i < n; i++) {
        std::set<int> bad_ind, next;
        for (int cur: curs) {
            auto cur_ind = ind.find(cur);
            if (cur_ind == ind.end())
                continue;
            int prev_ind = *std::prev(cur_ind), nextIdx = *std::next(cur_ind);
            if (elements[prev_ind] + elements[nextIdx] > limits[cur]) {
                bad_ind.insert(cur);
                next.insert(prev_ind);
                next.insert(nextIdx);
            }
        }
        printf("%lu ", bad_ind.size());
        for (int elem: bad_ind)
            ind.erase(elem);
        curs = next;
    }
    printf("\n");
    return 0;
}
