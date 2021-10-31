#!/usr/bin/env python
# -*- coding: utf-8 -*-

w,l = map(int, input().split())
a = list(map(int, input().split()))

m = sum(a[0:l])
s = m

for i in range(1,w-l):
    s =  s -a[i-1]+a[i+l-1]
    if s < m: m =s 
print(m)


