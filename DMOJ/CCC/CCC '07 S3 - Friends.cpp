#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	int people[10000];
	int visited[10000];
	for (int a = 0; a < 10000; a++) {
		visited[a] = -1;
	}

	for (int a = 0; a < N; a++) {
		int q, p;
		cin >> q >> p;
		people[q] = p;
	}

	int i = 0;
	for (;;) {
		i++;
		int x, y;
		cin >> x >> y;
		if (x == 0 && y == 0)
			break;
		int cur = x;
		int count = -1;
		for (;;) {
			if (visited[cur] == i) {
				count = -1;
				break;
			} else if (cur == y)
				break;
			else {
				visited[cur] = i;
				count++;
				cur = people[cur];
			}
		}

		if (count == -1)
			cout << "No\n";
		else cout << "Yes " << count << "\n";
	}
}