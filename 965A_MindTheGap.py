#!/usr/bin/env python
# -*- coding: utf-8 -*-

n,s = map(int, input().split())
r = 0

for _ in range(n):
    h,m = map(int, input().split())
    t = 60*h+m
    if t > r + s:
        break
    r=t+s+1
print(r//60, r%60)
