#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
	int s_size, max_changes;
	cin >> s_size >> max_changes;
	string s;
	cin >> s;

	if (max_changes == 0)
	{
		cout << s << "\n";
		return 0;
	}

	if (s_size == 1)
	{
		cout << "0\n";
		return 0;
	}

	int changes = 0;
	if (s[0] != '1')
	{
		s[0] = '1';
		changes++;

		if (changes == max_changes)
		{
			cout << s << "\n";
			return 0;
		}
	}

	for (int i = 1; i < s_size; ++i)
	{
		if (s[i] != '0')
		{
			s[i] = '0';
			changes++;

			if (changes == max_changes)
			{
				cout << s << "\n";
				return 0;
			}
		}
	}

	cout << s << "\n";
	return 0;
}