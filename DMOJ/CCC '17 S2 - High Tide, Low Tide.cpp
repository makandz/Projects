#include <bits/stdc++.h>

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

	float N;
	cin >> N;
	vector<int> list(N);

	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		list[i] = a;
	}

	sort(list.begin(), list.end());

	int half = ceil(N / 2);
	int cons = 0;

	int temp = N;
	cons = !((temp % 2) == 0) ? 1 : 0;

	vector<int> v1;
	v1 = vector<int>(list.begin(), list.end() - half + cons);
	reverse(v1.begin(), v1.end());

	vector<int> v2;
	v2 = vector<int>(list.begin() + half, list.end());

	for (int i = 0; i < half - cons; i++) {
		cout << v1[i] << " ";
		cout << v2[i];
		if (i != half - 1)
			cout << " ";
	}

	if (cons)
		cout << " " << v1[v1.size() - 1];

	cout << "\n";

	return 0;
}
