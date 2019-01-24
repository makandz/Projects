#include <iostream>
#include <string>

using namespace std;

int vowel(string inp) {
	return (inp == "a" || inp == "e" || inp == "i" || inp == "o" || inp == "u" || inp == "y");
}

int main() {
	string val, pop, con;
	for (;;) {
		cin >> val;
		if (val == "quit!")
			break;
		else if (val.size() > 4) {
			pop = val.substr(val.size() - 2);
			con = val.at(val.size() - 3);
			if (vowel(con) || pop != "or")
				cout << val << "\n";
			else {
				cout << val.substr(0, val.size() - 2) + "our\n";
			}
		} else cout << val << "\n";
	}

	// -------------------------------
	ios::sync_with_stdio(0);
	cin.tie(0);
	// -------------------------------
	return 0;
}