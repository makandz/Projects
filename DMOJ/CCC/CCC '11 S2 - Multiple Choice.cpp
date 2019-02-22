#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a;
    int d = 0;
    char c;
    cin >> a;
    vector<int> b(a);

    for (int i = 0; i < a; i++) {
        cin >> c;
        b[i] = c;
    }

    for (int i = 0; i < a; i++) {
        cin >> c;
        if (b[i] == c) ++d;
    }

    cout << d;
    return 0;
}