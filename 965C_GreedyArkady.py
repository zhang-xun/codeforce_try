#!/usr/bin/env python
# -*- coding: utf-8 -*-

n,k,M,D = map(int, input().split())
# n:  the number of candies 
# k:   the number of people
# M:  the maximum number of candies given to a person at once
# D: he maximum number of times a person can receive candies.

a  = max([ d* min(M, n//(k*(d-1)+1) )   for d in range(1,D+1)])
# n//(k*(d-1_+1)   k*x(d-1)+x<n-->
#                  x(kd-k+1)<n
#                 x<n/(k(d-1)+1)
# 理想状态下： 最后一次结束刚好到达第一个人取完，剩余的不够第二人再取
print(a)

