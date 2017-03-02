#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    times = int(input())
    capacity = 0
    max_capacity = 0
    for i in range(times):
        out_number, in_number = input().split()
        capacity += (int(in_number)-int(out_number))
        if capacity > max_capacity:
            max_capacity = capacity
    print(max_capacity)



def count():
    for i in range(1000000000):
        if i % 2 == 1:
            if i % 3 == 0:
                if i % 4 == 1:
                    if i % 5 == 3:
                        if i % 6  == 3:
                            if i % 7 == 0:
                                if i % 8 == 1:
                                    if i % 9 == 0:
                                        print(i)



if __name__ == "__main__":
    #main()
    count()