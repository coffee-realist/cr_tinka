#include <iostream>
#include <unordered_map>
#include <vector>
#include <cstdlib>
#include <ctime>
#pragma GCC optimize("Ofast")

int lcs(int n, int m, std::vector<int>& lst_1, std::vector<int>& lst_2) {
    int mx = std::min(n, m);
    while (mx > 0) {
        for (int ind = 0; ind < n - mx + 1; ind++) {
            for (int j = 0; j < m - mx + 1; j++) {
                if (lst_1[n - ind] + lst_2[m - mx - j] == lst_2[m - j] + lst_1[n - mx - ind]) {
                    return mx;
                }
            }
        }
        mx -= 1;
    }
    return mx;
}

int get_hash() {
    return std::rand();
}

int main() {
    std::srand(std::time(0));
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int m;
    std::cin >> m;
    std::vector<int> b(m);
    for (int i = 0; i < m; i++) {
        std::cin >> b[i];
    }
    std::unordered_map<int, int> hashes;
    hashes[a[0]] = get_hash();
    std::vector<int> lst_1(n + 1, 0);
    lst_1[1] = hashes[a[0]];
    std::vector<int> lst_2(m + 1, 0);
    if (hashes.find(b[0]) == hashes.end()) {
        hashes[b[0]] = get_hash();
    }
    lst_2[1] = hashes[b[0]];
    for (int i = 2; i < n + 1; i++) {
        int cur = a[i - 1];
        if (hashes.find(cur) == hashes.end()) {
            hashes[cur] = get_hash();
        }
        lst_1[i] = lst_1[i - 1] + hashes[cur];
    }
    for (int i = 2; i < m + 1; i++) {
        int cur = b[i - 1];
        if (hashes.find(cur) == hashes.end()) {
            hashes[cur] = get_hash();
        }
        lst_2[i] = lst_2[i - 1] + hashes[cur];
    }
    std::cout << lcs(n, m, lst_1, lst_2) << std::endl;
    return 0;
}

