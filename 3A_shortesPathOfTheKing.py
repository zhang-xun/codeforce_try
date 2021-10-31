#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    startpoint = [ i for i in input()] 
    endpoint =[ j for j in input()] 
    x_distance = ord(startpoint[0]) - ord(endpoint[0]) 
    y_distance =  int(startpoint[1]) - int(endpoint[1]) 
    x_abs_distance = abs(ord(startpoint[0]) - ord(endpoint[0]))
    y_abs_distance = abs(int(startpoint[1]) - int(endpoint[1]))

    print(max(x_abs_distance, y_abs_distance))

    while x_distance != 0 or y_distance != 0:
        r = ""
        if x_distance < 0: r="R"; x_distance+=1
        if x_distance > 0: r="L"; x_distance-=1
        if y_distance < 0: r+="U"; y_distance +=1
        if y_distance > 0: r+="D"; y_distance -= 1
        print(r) 



if __name__ == "__main__":
    main()
