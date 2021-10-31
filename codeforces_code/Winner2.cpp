#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

string names[1024];
int score[1024],_max;
map<string,int> input;
map<string,int>::iterator it;
int main()
{

	int times;
	cin>>times;
	vector<string> v;
	for(int i = 0; i < times; i++)
	{
		cin>>names[i]>>score[i];
		input[names[i]]+=score[i];
	
	}
	

	

	for(it=input.begin();it!=input.end();it++)
	{
		//cout<<(*it).first<<(*it).second<<endl;	
		if(_max < (*it).second)
		{
			v.clear();
			_max = (*it).second;
			v.push_back((*it).first);
		}
		else if(_max == (*it).second)
			v.push_back((*it).first);

	}

	/*
	for(int i = 0; i < v.size(); i++)
	{

		cout<<v[i]<<endl;
	}
	*/

	input.clear();
	for(int i = 0; i < times; i++)
	{
		input[names[i]]+=score[i];
		for(int j = 0; j < v.size(); j++)
		{
			if(names[i] == v[j] && input[names[i]] >= _max )
			{
				cout << names[i]<<endl;
				return 0;
			}	
		}
	
	}



	return 0;
}
