#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char const *argv[]){
	int T, N, M;
	cin >> T;
	for (int i = 0; i < T; ++i){
		cin >> N;
		cin >> M;

		std::vector<int> list1;
		std::vector<int> list2;

		for (int j = 0; j < N; ++j){
			int element;
			cin >> element;
			list1.push_back(element);
		}

		for (int j = 0; j < M; ++j){
			int element;
			cin >> element;
			list2.push_back(element);
		}

		int remove = 0;

		for (int j = 0; j < N; ++j){
			std::vector<int>::iterator it = find(list2.begin(), list2.end(), list1[j]);

			if (it == list2.end()){
				remove++;
			}
			else{
				list2.erase(it, it+1);
			}

		}
		remove += list2.size();

		cout << remove << "\n";

	}
	return 0;
}