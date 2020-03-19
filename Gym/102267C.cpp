#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
int main(int argc, char const *argv[]) {
  ll a,b;
  cin>>a>>b;
  ll cont=0;
  while(a>0){
    a = a/b;
    cont++;
  }
  cout<<cont<<endl;
  return 0;
}