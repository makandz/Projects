#include <iostream>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, k;
    cin >> N >> k;
    int s = N;

    for (int i = 1; i <= k; i++) {
        s += (N * (pow(10, i)));
    }

    cout << s;

    return 0;
}