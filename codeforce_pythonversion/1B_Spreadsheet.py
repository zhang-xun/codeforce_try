#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
like excel spreadsheet, A-Z after numbers
"""

import string

def main():
    count = int(input())
    for i in range(count):
        string1 = input()
        if string1.startswith('R'):
            flag = 2
            result1 = []
            for i in range(1,len(string1)):
                if string1[i] == "C":
                    flag = i
            R2Searchl = string1[1:flag]
            R2Searchr = string1[flag+1:]
            if int(R2Searchr) >26:
                result1.append(string.ascii_uppercase[int(R2Searchr)//26-1])
            result1.append(string.ascii_uppercase[int(R2Searchr)%26-1])
            result1.append(R2Searchl)
            
            print("".join(result1))
            #print(R2Searchl,"  ",R2Searchr)
        else:
            flag2 = 0
            result2 = []
            result2.append("R")
            for i in range(len(string1)):
                if string1[i].isdigit():
                    flag2 = i
                    break
            
            #print(flag2)
            Searchl2R = (string1[:flag2])
            Searchr2R = string1[flag2:]
            result2.append(Searchr2R)
            #print(Searchl2R,":",Searchr2R)
            result2.append("C")
            sum  = 0
            
            for i in range(len(Searchl2R)):
                
                index = string.ascii_uppercase.index(Searchl2R[i])
                sum += 26**(len(Searchl2R)-i-1) * (index+1)
            result2.append(str(sum))
            print("".join(result2))










if __name__ == "__main__":
    main()
