#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <string>

#pragma GCC optimize "Ofast"
#pragma GCC optimize "unroll-loops"
#pragma GCC optimize "omit-frame-pointer"
#pragma GCC optimize "prefetch-loop-arrays"
#pragma GCC target "sse,sse2,sse3,sse4,abm,avx,aes,sse4a,sse4.1,sse4.2,mmx,popcnt,tune=native"
using namespace std;

struct Comp {
	bool operator()(const pair<int, string> &a, const pair<int, string> &b) {
		if (a.first != b.first)
			return a.first < b.first;
		else return a.second > b.second;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	Comp comp;

	int amount;
	string s;
	int R, S, D, calc;
	cin >> amount;
	if (amount == 0)
		return 0;
	vector<pair<int, string>> list(amount);

	for (int i = 0; i < amount; i++) {
		cin >> s >> R >> S >> D;
		calc = (2 * R) + (3 * S) + D;
		list[i] = pair<int, string>(calc, s);
	}

	sort(list.rbegin(), list.rend(), comp);

	if (list[0].first == list[1].first) {
		if (list[0].second < list[1].second) {
			cout << list[0].second << "\n" << list[1].second << "\n";
		} else
			cout << list[1].second << "\n" << list[0].second << "\n";
	} else
		cout << list[0].second << "\n" << list[1].second << "\n";

	return 0;
}