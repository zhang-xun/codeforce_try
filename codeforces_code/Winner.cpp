#include <iostream>
#include <vector>
#include <string>
using namespace std;
using std::string;

int main()
{
	int times = 0;
	cin>>times;

	vector<string> names(times);
	vector<int> score(times);
	for(int i = 0; i < times; i++)
	{
		cin>>names[i]>>score[i];

	}

	//内部类，字典，泛型，排序
	//
	//引用，引用参数，virtual ， = 0，const
	
	for(int  i=0; i<times; i++)
	{
		for(int j=i+1; j<times; j++)
		{
			if(names[i] ==  names[j])
			{
				score[j]=score[i]+score[j];
			}
		}
	}
	int maxi=score[0];
	string maxs=names[0];
//	cout<< "before:" << maxs<<endl;
	for(int  i = 1; i<times; i++)
	{
		if(maxi<score[i])
		{
			maxi=score[i];
			maxs=names[i];
		}
	}
	/*
	for(int i=0; i<times; i++)
	{
		cout<<names[i]<<score[i]<<endl;
	}
	*/
	cout<<maxs<<endl;

	return 0;
}
