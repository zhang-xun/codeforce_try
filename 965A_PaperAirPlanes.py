#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

k, n , s, p = [int(i) for i in input().split()]
"""
the number of people, 
the number of airplanes each should make,
the number of airplanes that can be made using one sheet 
the number of sheets in one packg,
"""

sheet_one_person = math.ceil(n / s)
total_package = math.ceil(k * sheet_one_person / p)
print(total_package)

