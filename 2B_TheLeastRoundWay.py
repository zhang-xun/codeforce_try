#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
"""
There is a square matrix n × n, consisting of non-negative integer numbers. You should find such a way on it that

starts in the upper left cell of the matrix;
each following cell is to the right or down from the current cell;
the way ends in the bottom right cell.
Moreover, if we multiply together all the numbers along the way, the result should be the least "round". In other words, it should end in the least possible number of zeros.

Input
The first line contains an integer number n (2 ≤ n ≤ 1000), n is the size of the matrix. Then follow n lines containing the matrix elements (non-negative integer numbers not exceeding 109).

Output
In the first line print the least number of trailing zeros. In the second line print the correspondent way itself.

there is a square with numbers inside. We are to find a way with the minimal sum of the number over the way. This is classical dynamic programming problem. Let's consider that A[r,c] is the number in cell (r,c) and D[r,c] is the answer for this cell. Then 

D[r,c] = min(D[r-1,c],D[r,c-1]) + A[r][c]
"""
def fpow(x,b):
    if not x:
        return 1
    result = 0
    while not x % b:
        x = x // b
        result += 1
    return result



def main():
    n = int(input())
    dp2 = [float("inf")]*(n+1);path2=[]
    dp5 = [float("inf")]*(n+1);path5=[]
    dp2[0]=dp5[0]=0

if __name__ == "__main__":
    main()
