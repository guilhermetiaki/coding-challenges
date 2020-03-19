#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{
	int n;

	cin >> n;

	std::vector<bool> prime(n+1, true);

	prime[0] = false;
	prime[1] = false;

	int p = 2;

	while(p*p <= n+1)
	{
		if (prime[p] == true)
		{
			for (int i = p*p; i < n+1; i = i + p)
			{
				prime[i] = false;
			}
		}
		p++;
	}

	for (int i = 0; i < prime.size(); ++i)
	{
		if (prime[i] && prime[n-i])
		{
			cout << i << " " << n-i << "\n";
			return 0;
		}
	}

	cout << "-1\n";


	return 0;
}