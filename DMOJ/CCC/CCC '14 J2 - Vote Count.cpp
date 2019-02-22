#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a;
    int A = 0;
    int B = 0;
    string b;
    cin >> a >> b;

    for (int i = 0; i < a; i++) {
        if (b[i] == *"A") A++;
        else B++;
    }

    if (A > B) cout << "A\n";
    else if (A == B) cout << "Tie\n";
    else cout << "B\n";
    
    return 0;
}