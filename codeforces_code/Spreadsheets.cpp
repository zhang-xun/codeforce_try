#include <math.h>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

string  convert_to_string(string s)
{
	int temp = atoi(s.c_str());
	// 10 --> 26
	string result = "";
	while( temp > 0)
	{
		int m = temp % 26;
		if (m == 0)
			m = 26;
		result = char(m+64) +result;
		temp = (temp-m) /26;

	}
	return result;
	
	
}


long convert_to_long(string s)
{	
	long result =0;
	
	for(int i = s.length()-1,w=0; i>=0; i--,w = w+1)
	{
		//cout<< "w:"<<w <<endl;
		//cout<< (int)s[i] - 64 <<endl;
		//cout << "pow:"<<pow(26,w)<<endl;
		result = ((int)s[i]-64)*pow(26,w)+result;
	}

	return result;
}

int main()
{
	int n;
	string temp;
	vector<string> output(n);
	cin >> n;
	for(int i=0; i< n; i++)
	{
		cin >> temp;
		if ( temp[0] == 'R' && (temp[1] >= '0' && temp[1] <= '9') && temp.find('C') < temp.size()-1 )
		{
			string x_string = temp.substr(1,temp.find('C')-1);
			string y_string = temp.substr(temp.find('C')+1);
			
			cout<< convert_to_string(y_string)  << x_string <<endl;

		}

		else
		{
			string row_string ,col_string;
			for(int i = 0; i < temp.size(); i++)
			{
				if(temp[i] >= '0' && temp[i] <= '9')
				{
					row_string = temp.substr(i);
					//cout<<"row_string"<<row_string<<endl;
					break;	
				}
				else
				{
					col_string +=temp[i];
				}
			}

			cout<< "R" <<row_string << "C" << convert_to_long(col_string) <<endl;

		}

	}
	return 0;
}
