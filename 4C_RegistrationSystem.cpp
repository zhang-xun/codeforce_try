#include <iostream>
#include <string>
#include <map>

using namespace std;

map<string, int> m;
int n;
string s;
int main()
{
	cin >> n;
	while(n--)
	{
		cin >> s;
		if (m[s]++)
			cout << s<<m[s]-1;
		else
			cout <<"OK";
	
		cout << endl;	
	}
	/*	
	map<string,int>::iterator iter;
	for(iter = m.begin(); iter != m.end(); iter++)
	{
		cout << iter->first << " " << iter->second << endl;
	}

	*/
	return 0;
}
