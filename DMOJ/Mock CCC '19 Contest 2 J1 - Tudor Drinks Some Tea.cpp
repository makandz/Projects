#include <iostream>
#include <vector>

#pragma GCC optimize "Ofast"
#pragma GCC optimize "unroll-loops"
#pragma GCC optimize "omit-frame-pointer"
#pragma GCC optimize "prefetch-loop-arrays"
#pragma GCC target "sse,sse2,sse3,sse4,abm,avx,aes,sse4a,sse4.1,sse4.2,mmx,popcnt,tune=native"
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int c = 0;
	char a;
	for (int i = 0; i < 5; i++) {
		cin >> a;
		if (a == 'P') ++c;
	}
	cout << c << "\n";

	return 0;
}