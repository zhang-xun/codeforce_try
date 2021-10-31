#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    total_days , hours = [int(i) for i in input().split() ]
    min_hour = []
    max_hour = []

    for i in range(total_days):
        x, y = [int(x) for x in input().split()]
        min_hour.append(x)
        max_hour.append(y)
    if sum(max_hour ) < hours or sum(min_hour) > hours:
        print("NO")
        exit()
    hours -= sum(min_hour)
    for i in range(total_days):
        add = min(max_hour[i]-min_hour[i],hours)
        min_hour[i] = str(min_hour[i]+add)
        hours -= add
    print("YES")
    print(" ".join(min_hour))


if __name__ == "__main__":
    main()
