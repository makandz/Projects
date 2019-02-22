#include <iostream>

using namespace std;

int main() {
	int a, b;
	cin >> a >> b;

	if (a > 0 && b > 0)
		cout << 1;
	else if (a < 0 && b > 0)
		cout << 2;
	else if (a < 0 && b < 0)
		cout << 3;
	else
		cout << 4;

	// -------------------------------
	ios::sync_with_stdio(0);
	cin.tie(0);
	// -------------------------------
	return 0;
}