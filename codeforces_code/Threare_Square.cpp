#include <iostream>

using namespace std;

int main()
{
	long  long n,m,a;
	long long result;
	cin >> n >> m >> a;


	result=(m/a+(m%a==0?0:1))*(n/a+(n%a==0?0:1));

	cout<<result<<endl;
	return 0;
}
