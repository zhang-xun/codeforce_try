n,k = map(int,input().split())
r = range(n)

def auxiliary(strings, index):
    leftIndex = max(0,index-k+1)
    c = strings.rfind("#",leftIndex,index+1)
    rightIndex = min(n, index+k)
    d = strings.find("#",index, rightIndex)
    if c < 0: c = leftIndex-1
    if d < 0: d = rightIndex
    return max(0, d - c - k)

a = [input() for _ in r]
b = ["".join(_) for _ in zip(*a)]
tempt, i , j = max([(auxiliary(a[i],j)+auxiliary(b[j],i),i,j)for i in r for j in r])
print(i+1, j+1)
