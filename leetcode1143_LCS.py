def main(text1, text2):
    #border
    m,n = len(text1), len(text2)
    dp  = [[0]*(n+1) for i in range(m+1)]
    #initial value
    for i in range(m+1):
        dp[i][0] = 0
    for j in range(n+1):
        dp[0][j] = 0

    #dp
    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]


if __name__ == "__main__":
    #print(main("abcde","ace"))
    #print(main("abc","abc"))
    #print(main("abc","def"))
    print(main("bl","yby"))