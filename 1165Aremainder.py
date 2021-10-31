#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    n,x,y = map(int, input().split())
    s = list(map(int ,input()))
    print(sum(s[-x:]) - 2*s[-y-1] +1 )



if __name__ == "__main__":
    main()
