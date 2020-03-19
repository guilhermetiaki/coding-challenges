#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;

	cin >> T;

	for (int i = 0; i < T; ++i)	{
		string stringA, stringB;
		cin >> stringA >> stringB;
		int match_count = 0;
		vector<int> match_index;

		if (stringA.size() >= stringB.size()){
			for (int j = 0; j < stringA.size() - stringB.size() + 1; ++j){
				bool found = true;

				for (int k = 0; k < stringB.size(); ++k){
					if (stringA[j+k] != stringB[k]){
						found = false;
						break;
					}
				}
				if (found == true){
					match_count++;
					match_index.push_back(j+1);
				}

			}
		}



		if (match_count > 0){
			cout << match_count << endl;
			for (int j = 0; j < match_index.size(); ++j){
				cout << match_index[j] << " ";
			}
			cout << endl;
		}
		else{
			cout << "Not Found" << endl;
		}
		cout << endl;

	}

	return 0;
}