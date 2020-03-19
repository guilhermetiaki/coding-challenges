#include <iostream>
#include <cmath>
#include <vector>

using namespace std;
int main(int argc, char const *argv[]){
	int n, queries;

	cin >> n >> queries;

	vector<vector<int> > elements(n+1, vector<int> (pow(2,n)));

	for (int i = 0; i < pow(2,n); ++i){
		int tmp;
		cin >> tmp;
		elements[0][i] = tmp;
	}

	for (int i = 0; i < n; ++i){
		if (i % 2 == 0){
			for (int j = 0; j < pow(2,n-i); j+=2){
				elements[i+1][j/2] = elements[i][j] | elements[i][j+1];
			}
		}
		else{
			for (int j = 0; j < pow(2,n-i); j+=2){
				elements[i+1][j/2] = elements[i][j] ^ elements[i][j+1];
			}
		}

	}

	for (int q = 0; q < queries; ++q){
		int b, p;
		cin >> b >> p;
		b = b-1;
		elements[0][b] = p;

		for (int i = 0; i < n; ++i){
			if (i % 2 == 0){
				elements[i+1][b/2] = elements[i][b/2 * 2] | elements[i][b/2 * 2 + 1];
			}
			else{
				elements[i+1][b/2] = elements[i][b/2 * 2] ^ elements[i][b/2 * 2 + 1];
			}
			b /= 2;
		}

		cout << elements[n][0]<< endl;
	}

	return 0;
}