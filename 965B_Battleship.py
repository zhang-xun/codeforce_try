#!/usr/bin/env python
# -*- coding: utf-8 -*-

n , k = [ int(i) for i in input().split()]
# n: the size of the field 
# k: the size of the ship
def auxiliary(strings, index):
    left_index = max(0, index - k + 1)
    c = strings.rfind("#",left_index,index+1)
    right_index = min(n, index+k)
    d = strings.find("#",index, right_index)
    if c < 0: c = left_index - 1
    if d < 0: d = right_index 
    return max(0, d-c-k)

r = range(n)
a = [input() for _ in r]
b = ["".join(_) for _ in zip(*a)]
max_index, i , j = max([(auxiliary(a[i],j)+auxiliary(b[j],i),i,j) for i in r for j in r])
print(max_index, i+1, j+1)

