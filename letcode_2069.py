def numWays( n: int) -> int:
    if n == 0 or n == 1:
        return 1
    dp =[0] * (n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[n]
def numWays2(n):
    a, b = 1, 1
    for _ in range(1, n):
        a, b = b, (a + b) % 1000000007
    return b
for i in range(45):
    print(numWays(i))
    print(numWays2(i))
    print("\n")