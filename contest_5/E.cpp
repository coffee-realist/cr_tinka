#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
using namespace std;

vector<int> build_suffix_array(string s) {
    s += "$";
    int n = s.length();
    vector<int> ranks(n);
    for (int i = 0; i < n; i++) {
        ranks[i] = (int)s[i];
    }
    vector<int> sa(n);
    for (int i = 0; i < n; i++) {
        sa[i] = i;
    }
    auto sort_on_kth_character = [&](int ind) {
        vector<tuple<int, int, int>> pairs(n);
        for (int j = 0; j < n; j++) {
            pairs[j] = make_tuple(ranks[j], (j + ind < n) ? ranks[j + ind] : -1, j);
        }
        sort(pairs.begin(), pairs.end());
        vector<int> sorted_indices(n);
        for (int j = 0; j < n; j++) {
            sorted_indices[j] = get<2>(pairs[j]);
        }
        return sorted_indices;
    };
    int k = 1;
    while (k < n) {
        sa = sort_on_kth_character(0);
        vector<int> tmp_ranks(n);
        int rank = 0;
        for (int i = 1; i < n; i++) {
            int prev = sa[i - 1];
            int curr = sa[i];
            if (ranks[prev] != ranks[curr] || ranks[prev + k] != ranks[curr + k]) {
                rank += 1;
            }
            tmp_ranks[curr] = rank;
        }
        ranks = tmp_ranks;
        if (ranks[sa[n - 1]] == n - 1) {
            break;
        }
        k *= 2;
    }
    return sa;
}

vector<int> find_with_one_mismatch(vector<int> sa, string p, string t) {
    vector<int> positions;
    int len_p = p.length();
    int n = t.length();
    auto match_with_mismatch = [&](int ind) {
        int mismatch_count = 0;
        for (int j = 0; j < len_p; j++) {
            if (ind + j >= n || t[ind + j] != p[j]) {
                mismatch_count += 1;
                if (mismatch_count > 1) {
                    return false;
                }
            }
        }
        if (mismatch_count <= 1) {
            return true;
        }
        else {
            return false;
        }
    };
    for (int idx = 0; idx < sa.size(); idx++) {
        int i = sa[idx];
        if (i + len_p <= n && match_with_mismatch(i)) {
            positions.push_back(i + 1);
        }
    }
    return positions;
}

int main() {
    string p, t;
    cin >> p >> t;
    vector<int> suffix_array = build_suffix_array(t);
    vector<int> result = find_with_one_mismatch(suffix_array, p, t);
    cout << result.size() << endl;
    sort(result.begin(), result.end());
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    return 0;
}

