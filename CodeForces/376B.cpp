#include <iostream>
using namespace std;

int main(){
    int debt_table[100], n, m;
    cin >> n >> m;

    for (int i = 0; i < 100; ++i)    {
        debt_table[i] = 0;
    }

    int a,b,c;
    for (int i = 0; i < m; ++i){
        cin >> a >> b >> c;
        debt_table[a-1]-=c;
        debt_table[b-1]+=c;
    }

    int sum=0;
    for(int i=0; i < n ; i++){
        if(debt_table[i]>0)
            sum += debt_table[i];
    }
    cout << sum << endl;

    return 0;
}