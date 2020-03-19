#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main(int argc, char const *argv[])
{


	int num_sacos, competidores, pipocas_t;
	cin >> num_sacos >> competidores >> pipocas_t;
	std::vector<int> sacos;
	int soma_sacos = 0;
	int k = num_sacos;

	while (k--){
		int aux;
		cin >> aux;
		soma_sacos += aux;
		sacos.push_back(aux);
	}

	std::map<int, bool> resposta;
	int chute_t = soma_sacos/pipocas_t;
	int atual = chute_t;
	int lim_sup = atual+51;
	int lim_inf = 0;
	atual = (lim_sup+lim_inf)/2;

	while (lim_sup != atual && lim_inf != atual){
		int chute_pipocas = atual*pipocas_t;
		std::vector<int> aux = sacos;
		int j = 0;
		for (int i = 0; i < competidores; i++){
			int pode_comer = chute_pipocas;
			while ((pode_comer >= 0) && (j < num_sacos)){
				if (aux[j] <= pode_comer){
					pode_comer -= aux[j];
					aux[j] = 0;
					j++;
				} else {
					break;
				}
			}
		}

		if (aux[aux.size()-1] == 0){
			resposta[atual] = true;
			lim_sup = atual;
			atual = (lim_sup+lim_inf)/2;
		}
		else {
			std::map<int, bool>::iterator it;
			it = resposta.find(atual);
			if (it != resposta.end()){
				break;
			}
			resposta[atual] = false;
			lim_inf = atual;
			atual = (lim_sup+lim_inf)/2;
		}
	}

	if (resposta[lim_sup] == true){
		cout << lim_sup << endl;
	}
	else {
		cout << lim_inf << endl;
	}

	return 0;
}