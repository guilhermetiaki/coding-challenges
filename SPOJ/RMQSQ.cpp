#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[]){
	int N;

	cin >> N;

	std::vector<int> list;
	for (int i = 0; i < N; ++i)
	{
		int element;
		cin >> element;
		list.push_back(element);
	}

	int Q;
	cin >> Q;

	for (int i = 0; i < Q; ++i)
	{
		int begin, end;

		cin >> begin;
		cin >> end;

		int min = list[begin];
		for (int j = begin + 1; j <= end; ++j)
		{
			if (list[j] < min)
			{
				min = list[j];
			}
		}
		cout << min << "\n";
	}

	return 0;
}