#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct computer {
    int speed;
    string name;
};

int main() {
    int amount;
    string s;
    int R, S, D, calc;
    cin >> amount;
    if (amount == 0)
        return 0;
    vector<computer> list(amount);

    for (int i = 0; i < amount; i++) {
        cin >> s >> R >> S >> D;
        calc = (2 * R) + (3 * S) + D;
        list[i] = computer();
        list[i].speed = calc;
        list[i].name = s;
    }

    // sorting
    for (int a = 0; a < amount; a++) {
        for (int b = 0; b < amount - 1; b++) {
            if (list[b].speed < list[b + 1].speed)
                swap(list[b], list[b + 1]);
            else if (list[b].speed == list[b + 1].speed) {
                if (list[b].name > list[b + 1].name)
                    swap(list[b], list[b + 1]);
            }
        }
    }

    cout << list[0].name << "\n" << list[1].name << "\n";

    // -------------------------------
    ios::sync_with_stdio(0);
    cin.tie(0);
    // -------------------------------
    return 0;
}