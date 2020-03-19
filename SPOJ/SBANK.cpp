#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main(int argc, char const *argv[]){
	int t,n;

	cin >> t;

	for (int x = 0; x < t; ++x){
		cin >> n;

		std::vector<string> accounts;

		cin.ignore();
		for (int i = 0; i < n; ++i){
			string account;
			getline (cin, account);
			accounts.push_back(account);
		}

		sort(accounts.begin(), accounts.end());

		cout << accounts[0];
		int count = 1;
		for (int i = 1; i < accounts.size(); ++i){
			if (accounts[i].compare(accounts[i-1]) == 0){
				count++;
			}
			else{
				cout << " " << count << "\n";
				cout << accounts[i];
				count = 1;
			}
		}
		cout << " " << count << "\n\n";

	}
	return 0;
}