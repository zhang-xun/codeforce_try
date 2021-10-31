#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    input()
    s = list(map(int, input().split()))
    s.sort()
    ans = 0
    for i in s:
        if i > ans:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
