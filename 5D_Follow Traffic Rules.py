import math

def main():
    a,v = [int(i) for i in input().split()] 
    l,d,w = [int(i) for i in input().split()]
    if w > v: w = v
    x,t = calt(0,w,a,d)
    if x == d:
        print(go(0,v,a,l))
    else:
        print(t+go(w,v,a,(d-x)*0.5)*2+go(w,v,a,l-d))


def calt(v0,v1,a,x):
    t = (v1-v0)/a
    x0 = v0*t+0.5*a*t**2
    if x0 <  x: return x0,t
    else:
        return x,(math.sqrt(v0*v0+2*a*x)-v0)/a

def go(v0, v1, a, x):
    x0, t = calt(v0, v1,a,x)
    return t +(x-x0)/v1

if __name__ == "__main__":
    main()