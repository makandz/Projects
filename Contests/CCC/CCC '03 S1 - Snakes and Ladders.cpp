#include <iostream>

int main() {
    int loc = 1;
    while (true) {
        int a = 0;
        std::cin >> a;
        if (loc + a <= 100)
            loc += a;
        if (a == 0) {
            std::cout << "You Quit!\n";
            break;
        }
        else if (loc == 9)
            loc = 34;
        else if (loc == 54)
            loc = 19;
        else if (loc == 40)
            loc = 64;
        else if (loc == 67)
            loc = 86;
        else if (loc == 90)
            loc = 48;
        else if (loc == 99)
            loc = 77;
        std::cout << "You are now on square " << loc << "\n";
        if (loc == 100) {
            std::cout << "You Win!\n";
            break;
        }
    }
}