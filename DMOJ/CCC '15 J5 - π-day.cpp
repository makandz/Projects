#include <iostream>

#pragma GCC optimize "Ofast"
#pragma GCC optimize "unroll-loops"
#pragma GCC optimize "omit-frame-pointer"
#pragma GCC optimize "prefetch-loop-arrays"
#pragma GCC target "sse,sse2,sse3,sse4,abm,avx,aes,sse4a,sse4.1,sse4.2,mmx,popcnt,tune=native"
using namespace std;

int dab[251][251][251];

int func(int n, int k, int m) {
    if (n == k || k == 1)
        return 1;
    else if (dab[k][n][m] == 0) {
        for (int i = m; i * k <= n; ++i) {
            dab[k][n][m] += func(n - i, k - 1, i);
        }
    }
    return dab[k][n][m];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, k;
    cin >> n >> k;
    cout << func(n, k, 1);

    return 0;
}