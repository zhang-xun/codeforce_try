#include <iostream>
using namespace std;
int d,sumTime,a[100],b[100],k,x;
int add;
int main()
{
	cin>>d>>sumTime;
	for(int i = 0; i< d; i++)
	{
		cin>>a[i]>>b[i];
		k+=a[i];
		x+=b[i];
	}
	if (k > sumTime || x < sumTime)
	{
		cout <<"NO"<<endl;
		return 0;
	}

	sumTime -= k;
	int add;
	cout <<"YES"<<endl;
	for (int i = 0; i < d; i++)
	{
		add = min(b[i]-a[i],sumTime);
	 cout << a[i]+add<<" ";
	 sumTime -= add;
	}
	

	return 0;
}
