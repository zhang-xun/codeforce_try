#!/usr/bin/env python
# -*- coding: utf-8 -*-

a=[int(i) for i in input().split()]

def score(l):
    #  通过布尔值来计算数列中偶数的和 
    return sum(x*(x%2==0) for x in l)
result = 0
for i in range(14):
    templist = a[:]
    for j in range(13):
        # this importent  三元运算符
        templist[(i+j+1)%14] += templist[i]//14 + (1 if  (j+1)<=templist[i]%14   else 0)
    result = max(result, score(templist))
print(result)

