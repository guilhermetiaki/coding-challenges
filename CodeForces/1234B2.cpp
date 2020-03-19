#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;

int main(int argc, char const *argv[])
{
	int n_messages, max_lines;
	cin >> n_messages >> max_lines;

	deque<int> screen;

	set<int> screen_set;

	for (int i = 0; i < n_messages; ++i)
	{
		int sender_id;
		cin >> sender_id;

		if (screen_set.find(sender_id) == screen_set.end())
		{
			screen.push_front(sender_id);
			screen_set.insert(sender_id);
			if (screen.size() > max_lines)
			{
				screen_set.erase(screen.back());
				screen.pop_back();

			}
		}
	}

	int screen_size = screen.size();

	cout << screen_size << "\n";
	for (int i = 0; i < screen_size; ++i)
	{
		cout << screen[i] << " ";
	}
	cout << "\n";

	return 0;
}