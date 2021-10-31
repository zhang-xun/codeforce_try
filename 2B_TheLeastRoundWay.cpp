#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

#define Max 1007

using namespace std;
int dp[2][Max][Max],p[2][Max][Max];
int input_border, input_number;

void print(int x, int y, int k, int f)
{
	if (x==1 && y==1);
	else if (x == 1)
		print(x, y-1, k, 0);
	else if (y==1)
		print(x-1, y, k,1);
	else
	{
		if (dp[k][x][y] == dp[k][x-1][y] + p[k][x][y])
			print(x-1, y, k, 1);
		else
			print(x, y-1, k, 0);
	}

	if (f==3)
		return ;
	printf("%c", f?'D':'R');
}


int main()
{
	
	int flag = 0;
	int zero_x, zero_y;
	cin >> input_border; 

	for(int i = 1; i <= input_border; i++)
	{
		for(int j=1; j <= input_border; j++)
		{
			cin >> input_number;
			if (!input_number)
			{
				flag = 1;
				p[0][i][j]++;
				p[1][i][j]++;
				zero_x = i;
				zero_y = j;
				continue;
			}
			while(input_number % 2 ==0)
			{
				p[0][i][j]++;
				input_number/=2;
			}
			while(input_number % 5==0)
			{
				p[1][i][j]++;
				input_number/=5;
			}
		}
	}
	memset(dp, 0x7f, sizeof(dp));
/*
	for(int i = 1; i<= input_border; i++)
	{
	for (int j=1; j<= input_border; j++)
		cout << p[0][i][j];
	cout<<endl;
	}
	for(int i = 1; i<= input_border; i++)
	{
	for (int j=1; j<= input_border; j++)
		cout << p[1][i][j];
	cout<<endl;
	}


*/

	for (int k =0; k < 2; k++)
	{
		for (int i=1; i <= input_border; i++)
		{
			for(int j=1; j<= input_border; j++ )
			{
				if(i-1)
				{
					dp[k][i][j]=min(dp[k][i][j], dp[k][i-1][j]);
				}
				if(j-1)
					dp[k][i][j]=min(dp[k][i][j], dp[k][i][j-1]);
				if(i==j&&i==1)
					dp[k][i][j]=0;
				dp[k][i][j]+=p[k][i][j];
			}
		}
	}
	/*
	for(int i = 1; i<= input_border; i++)
	{
	for (int j=1; j<= input_border; j++)
		cout << dp[0][i][j]<<"\t";
	cout<<endl;
	}
	for(int i = 1; i<= input_border; i++)
	{
	for (int j=1; j<= input_border; j++)
		cout << dp[1][i][j]<<"\t";
	cout<<endl;
	}
	*/
	int ans=min(dp[0][input_border][input_border], dp[1][input_border][input_border] );
	if (ans>1 && flag)
	{
		cout << "1"<<endl;
		for(int i=1; i<zero_x; i++)
			cout <<"D";
		for(int j=1; j <zero_y ;j++)
			cout <<"R";
		for(int i=zero_x; i<input_border; i++)
			cout <<"D";
		for(int j=zero_y; j<input_border; j++)
			cout <<"R";

	}
	cout<<ans<<endl;
	if(dp[0][input_border][input_border]<dp[1][input_border][input_border])
		print(input_border, input_border, 0, 3);
	else
		print(input_border, input_border, 1, 3);
	return 0;
}

