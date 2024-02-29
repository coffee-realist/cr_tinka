#include <stdio.h>
#include <deque>
#pragma GCC optimize("Ofast")

using namespace std;
signed main()
{
    int n, query, id, q;
    scanf("%d", &n);
    deque<int> d;
    int database[100002];
    int out = 0;
    for (int i = 0; i < n; i++){
        scanf("%d", &query);
        if (query == 1){
            scanf("%d", &id);
            database[id] = d.size() + out;
            d.push_back(id);
        }
        else if (query == 2){
            d.pop_front();
            out++;
        }
        else if (query == 3)
            d.pop_back();
        else if (query == 4){
            scanf("%d", &q);
            printf("%d\n", database[q] - out);
        }
        else
            printf("%d\n", d.front());
    }
}
