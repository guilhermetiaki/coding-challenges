#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

int main(int argc, char const *argv[])
{
	int l,r;

	cin >> l >> r;

	for (int i = l; i <= r; ++i)
	{
		string x = to_string(i);
		unordered_set<char> x_set(x.begin(), x.end());
		if (x.size() == x_set.size()){
			cout << x << endl;
			return 0;
		}

	}
	cout << "-1" << endl;
	return 0;
}