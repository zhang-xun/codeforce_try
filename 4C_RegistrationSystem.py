#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    n = int(input())
    temp = dict()
    for i in range(n):
        input_name = input().strip()
        if input_name not in temp:
            temp.setdefault(input_name,0)
            print("OK")
        else:
            outtime = temp.get(input_name)
            temp[input_name]+=1
            print(input_name+str(outtime+1))


if __name__ == "__main__":
    main()
