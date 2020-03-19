#include <bits/stdc++.h>

using namespace std;

#define MAX 25
typedef long long ll;
int n;
int arr[MAX];


vector<int> getSum(int s) {
	vector<int> elems;
	elems.push_back(arr[s]);
	if (s == n-1) return elems;

	vector<int> others = getSum(s+1);
	for (int i = 0; i < others.size(); i++) elems.push_back(others[i]);
	int i = 0;
	for (int i = 0; i < others.size(); i++) {
		elems.push_back(arr[s] | others[i]);
	}
	return elems;
}

int main() {
	cin >> n;

	for (int i; i < n; i++) cin >> arr[i];

	vector<int> all = getSum(0);

	ll sum = 0;
	for (int i=0; i<all.size();i++) sum += all[i];

	cout << sum << endl;
	return 0;
}