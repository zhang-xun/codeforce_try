#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int times;
	cin>>times;

	vector<int> square(times*times);

	for(int i = 0; i < times*times; i++)
	{
		cin>>square[i];
	}



	return 0;
}
