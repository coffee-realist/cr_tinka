#include <string>
#include <iostream>
#include <algorithm>
#include <random>

using namespace std;

bool is_prime(int x){
    for (int i = 2; i <= x / i; i++)
        if (x % i == 0)
            return false;
}

int prev_prime(int x){
    while (true){
        x--;
        if (is_prime(x))
            return x;
    }
}

int main()
{
    string a, b;
    cin >> a >> b;
    int p = 79;
    int n = (int)max(b.size() * 2, a.size());
    vector<long long> pows1(1 + n);
    vector<long long> pows2(1 + n);
    int minn = int(2e9), maxx = int(2e9) + int(1e8);
    int m_1 = prev_prime(minn + (rand() % static_cast<int>(maxx - minn + 1)));
    int m_2 = prev_prime(minn + (rand() % static_cast<int>(maxx - minn + 1)));
    pows1[0] = 1 % m_1; pows2[0] = 1 % m_2;
    for (int i = 1; i <= n; i++){
        pows1[i] = int((1LL * pows1[i - 1] * p) % m_1);
        pows2[i] = int((1LL * pows2[i - 1] * p) % m_2);
    }
    vector<long long> b_sum_1(b.size() * 2 + 1);
    vector<long long> b_sum_2(b.size() * 2 + 1);
    b_sum_1[0] = 0; b_sum_2[0] = 0;
    for (int i = 1; i <= b.size() * 2; i++){
        b_sum_1[i] = (b_sum_1[i - 1] + b[i % b.size()] * 1LL * pows1[i - 1]) % m_1;
        b_sum_2[i] = (b_sum_2[i - 1] + b[i % b.size()] * 1LL * pows2[i - 1]) % m_2;
    }
    vector<long long> a_sum_1(a.size() + 1);
    vector<long long> a_sum_2(a.size() + 1);
    a_sum_1[0] = 0; a_sum_2[0] = 0;
    for (int i = 1; i <= a.size(); i++){
        a_sum_1[i] = (a_sum_1[i - 1] + a[i - 1] * 1LL * pows1[i - 1]) % m_1;
        a_sum_2[i] = (a_sum_2[i - 1] + a[i - 1] * 1LL * pows2[i - 1]) % m_2;
    }
    vector<pair<long long, long long>> occurrences;
    for (int i = b.size(); i < b.size() * 2; i++){
        long long r_1 = ((b_sum_1[i] - b_sum_1[i - b.size()] + m_1) * pows1[n - i]) % m_1;
        long long r_2 = ((b_sum_2[i] - b_sum_2[i - b.size()] + m_2) * pows2[n - i]) % m_2;
        pair <long long, long long> cur(r_1, r_2);
        occurrences.push_back(cur);
    }
    sort(occurrences.begin(), occurrences.end());
    int result = 0;
    for (int i = b.size(); i <= a.size(); i++){
        long long r_1 = ((a_sum_1[i] - a_sum_1[i - b.size()] + m_1) * pows1[n - i]) % m_1;
        long long r_2 = ((a_sum_2[i] - a_sum_2[i - b.size()] + m_2) * pows2[n - i]) % m_2;
        pair <long long, long long> cur(r_1, r_2);
        if (binary_search(occurrences.begin(), occurrences.end(), cur))
            result++;
    }
    cout << result << endl;
    return 0;
}
