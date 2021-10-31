#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    n,w,h  = [int(x) for x in input().split()]
    chain = []
    for i in range(n):
        chain.append([int(x) for x in input().split()])

    print(chain)



if __name__ == "__main__":
    main()
