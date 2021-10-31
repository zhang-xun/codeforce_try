#!/usr/bin/env python
# -*- coding: utf-8 -*-

n,A,B = map(int, input().split())
# n:  the number of holes,
# A: the volume of water Arkady will pour into the system
# B;  the volume he wants to get out of the first hole
s1,*s = map(int,input().split())
s.sort()
holes_block=0
total = sum(s[:])+s1
while True:
    # this process is important 
    vfr = (s1*A)/total

    if vfr>=B:
        print(holes_block)
        break
    holes_block += 1
    total -=  s[holes_block-1]
