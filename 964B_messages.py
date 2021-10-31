#!/usr/bin/env python
# -*- coding: utf-8 -*-

n, A, B, C, T = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
bank_acount = 0

for i in range(len(t)):
    bank_acount += A
    if C >= B: bank_acount += (T-t[i])*(C-B)

print(bank_acount)



    
