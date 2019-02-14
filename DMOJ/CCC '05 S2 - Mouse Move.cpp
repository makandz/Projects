#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int mx, my, x, y;
    int cx = 0;
    int cy = 0;
    cin >> mx >> my;

    for (;;) {
        cin >> x >> y;
        if (x == 0 && y == 0) break;
        cx += x;
        cy += y;
        if (cx < 0) cx = 0;
        if (cy < 0) cy = 0;
        if (cx > mx) cx = mx;
        if (cy > my) cy = my;
        cout << cx << " " << cy << "\n";
    }
    
    return 0;
}