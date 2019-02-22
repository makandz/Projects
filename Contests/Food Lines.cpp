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

	int M, P;
	cin >> M >> P;
	vector<int> a(M);

	for (int i = 0; i < M; i++)
		cin >> a[i];

	for (int i = 0; i < P; i++) {
		int small = 200;
		int loc;
		for (int q = 0; q < M; q++) {
			if (a[q] < small) {
				loc = q;
				small = a[q];
			}
		}

		cout << a[loc] << "\n";
		a[loc]++;
	}

	return 0;
}