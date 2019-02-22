#include <iostream>

int main() {
	int a, b;
	std::cin >> a >> b;
	if (a > b) std::cout << "CS452\n";
	else if (a < b) std::cout << "PHIL145\n";
}