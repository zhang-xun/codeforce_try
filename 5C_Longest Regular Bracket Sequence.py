from collections import deque
import heapq    


def main():
    m,b,s = 0,1,[-1]
    temp = input()
    for i,c in enumerate(temp):
        if c =="(":s.append(i)
        elif len(s)>1:
            s.pop()
            n = i-s[-1]
            if n > m: m,b = n,1
            elif m == n: b+=1
        else:s[0]= i
            
    print(" ".join([str(m),str(b)]))

if __name__ == "__main__":
    main()