#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char const *argv[])
{

	int voltas, num_placas;

	cin >> voltas >> num_placas;

	double total_placas = voltas*num_placas;

	for (int i = 1; i <= 9; i++){

		if (i == 9){
			cout << int(ceil(total_placas*((i*10)/double(100)))) << "\n";
		} else {
			cout << int(ceil(total_placas*((i*10)/double(100)))) << " ";
		}

	}


	return 0;
}