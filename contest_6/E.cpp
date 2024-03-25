#include <iostream>
#include <deque>
#include <cmath>
#include <limits>
#include <vector>
#pragma GCC optimize("Ofast")

int min_digit_sum_divisible_by_k(int k) {
    if (k == 1) {
        return 1;
    }
    int inf = std::numeric_limits<int>::max();
    std::vector<int> dp(k, inf);
    std::deque<int> d;
    for (int i = 1; i < 10; i++) {
        dp[i % k] = std::min(dp[i % k], i);
        d.push_back(i % k);
    }
    while (!d.empty()) {
        int p = d.front();
        d.pop_front();
        for (int digit = 0; digit < 10; digit++) {
            int new_p = (p * 10 + digit) % k;
            int new_sum = dp[p] + digit;
            if (new_sum < dp[new_p]) {
                dp[new_p] = new_sum;
                d.push_back(new_p);
            }
        }
    }
    if (dp[0] != inf) {
        return dp[0];
    } else {
        return k;
    }
}

int main() {
    int k;
    std::cin >> k;
    std::cout << min_digit_sum_divisible_by_k(k) << std::endl;
    return 0;
}

