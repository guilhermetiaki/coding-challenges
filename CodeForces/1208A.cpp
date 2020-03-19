#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
int main(int argc, char const *argv[])
{
	ll t;
	scanf("%lld",&t);
	ll aux=0;
	while(aux<t){
		ll a,b,n;
		scanf("%lld %lld %lld",&a,&b,&n);
		if(n%3==0) printf("%lld\n",a);
		else if(n%3==1) printf("%lld\n",b);
		else printf("%lld\n",a^b);
		aux++;
	}
	return 0;
}