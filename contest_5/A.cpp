#include <iostream>
#include <vector>
#include <string>
#pragma <Ofast>

using namespace std;

typedef unsigned long long ull;

unsigned long long get_hash(ull hashes[], ull pows[], int left, int right) {
    return hashes[right + 1] - hashes[left] * pows[right - left + 1];
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    int m;
    string s;
    cin >> s >> m;
    ull hashes[s.length() + 1];
    ull pows[s.length() + 1];
    const long long prime = 31;
    // const long long prime = 1000000009;
    hashes[0] = 0;
    pows[0] = 1;
    for (int i = 0; i < s.length(); ++i) {
        hashes[i + 1] = hashes[i] * prime + s[i];
        pows[i + 1] = pows[i] * prime;
    }
    for (int i = 0; i < m; ++i) {
        int left_1, right_1, left_2, right_2;
        cin >> left_1 >> right_1 >> left_2 >> right_2;
        left_1--; right_1--; left_2--; right_2--;
        if (get_hash(hashes, pows, left_1, right_1) == get_hash(hashes, pows, left_2, right_2))
            cout << "Yes" << endl;
        else
            cout << "No" << endl;
    }
    return 0;
}