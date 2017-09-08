__author__ = 'zhangxun'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
temp_list,name_scoreD = [],{}
for i in range(n):
    a,b = input().split()
    b = int(b)
    name_scoreD[a] = name_scoreD.get(a,0)+b
    temp_list.append([name_scoreD[a],a])
    m = max(name_scoreD.values())

for score,name in temp_list:
    if score >= m and name_scoreD[name] >= m:
        print(name)
        break

