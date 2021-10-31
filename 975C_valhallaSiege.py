#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bisect
from itertools import accumulate

n,q = map(int,input().split())
a = map(int, input().split())
s = map(int,input().split())

accumulate_a = list(accumulate(a))
accumulate_s = list(accumulate(s))
allkilled=0  # 记住那个被团灭的onedamage
result = []
for onedamage in accumulate_s:
    killedwarrior = bisect.bisect(accumulate_a,onedamage-allkilled)
    if killedwarrior == n:
        allkilled = onedamage
        result.append(n)
    else:
        result.append(n-killedwarrior)

print("\n".join(map(str,result)))

