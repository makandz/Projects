#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int amount, s;
    cin >> amount;
    if (amount == 0)
        return 0;
    vector<int> list(amount);

    for (int i = 0; i < amount; i++) {
        cin >> s;
        list[i] = s;
    }

    for (int i = 0; i < amount; i++)
        cout << list[i] << " ";
    cout << "\n";

    for (int a = 0; a < amount; a++) {
        for (int b = 0; b < amount - 1; b++) {
            if (list[b] > list[b + 1]) {
                swap(list[b], list[b + 1]);
                for (int i = 0; i < amount; i++)
                    cout << list[i] << " ";
                cout << "\n";
            }
        }
    }

    cout << "\n";

    return 0;
}