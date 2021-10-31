#include <iostream>
#include <string>
#include <map>
#include <vector>


using namespace std;

map<string,int>::iterator it;
map<string,int> dict;
vector<string> max_temp;
int main()
{
	int times;
	int _max;
	cin>>times;

	vector<string> names(times);
	vector<int> scores(times);
	for(int i =0; i < times; i++)
	{
		cin>>names[i]>>scores[i];
		dict[names[i]]+=scores[i];
	}


	for(it=dict.begin(); it!=dict.end();it++)
	{
		if( _max < (*it).second)
		{
			max_temp.clear();
			_max = (*it).second;
			max_temp.push_back((*it).first);
		}
		else if( _max == (*it).second)
		{
		
			max_temp.push_back((*it).first);
		}
	}

	dict.clear();
	for(int i = 0; i < times; i++)
	{
		dict[names[i]]+=scores[i];
		for(int j = 0; j < max_temp.size(); j++)
			{
				if(names[i]==max_temp[j] && dict[names[i]] >= _max)
				{
					cout << names[i];
					return 0;
				}
			}

	
	}



	return 0;
}
