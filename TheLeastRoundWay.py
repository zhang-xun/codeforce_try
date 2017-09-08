#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
"""
