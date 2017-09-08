#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

DEBUG = False 

def area(d):
    if len(d) < 3:
        return False
    a = 0.0
    p = 0.5 * (d[0] + d[1] + d[2])
    a = math.sqrt(p*(p-d[0])*(p-d[1])*(p-d[2]))
    return a

def circumcircle(x,y):
    distance = euclidean(x,y)
    triangle_area = area(distance)
    return distance[0] * distance[1] * distance[2] / (4 * triangle_area)
    
def euclidean(x,y):
    d = []
    d.append(math.sqrt((x[0]-x[1])**2 + (y[0]-y[1])**2))
    d.append(math.sqrt((x[0]-x[2])**2 + (y[0]-y[2])**2))
    d.append(math.sqrt((x[1]-x[2])**2 + (y[1]-y[2])**2))
    return d
def normal_sin_value(sin_value):
    if sin_value > 1:
        return 1.0
    elif sin_value < -1:
        return -1.0
    else:
        return sin_value
    
def centerAngle(d,radius):
    angle = []
    #print(type(d[0]), type(radius))
    #print(d[0]/(2*radius))
    #print(2 * math.asin( d[0] / (2*radius) ) )
    angle.append(2*math.asin(normal_sin_value(d[0]/(2*radius))))
    angle.append(2*math.asin(normal_sin_value(d[1]/(2*radius))))
    angle.append(2*math.pi - angle[0] - angle[1])
    if DEBUG:
        print(sum([a for a in angle]))
    return angle

def gcd(a,b):
    if a < 0.01:
        return b
    else:
        return gcd(math.fmod(b,a),a)
def main():
    
    # get the input data
    x = []
    y = []
    for i in range(3):
        temp_input = input().split() 
        x.append(float(temp_input[0]))
        y.append(float(temp_input[1]))

    # 1. calculate the length of the edge 
    # 2. calculate the area of the triangle
    # 3. calculate the radius of the circumcircle
    # 4. calculate the area of the Berland Circus

    edge_length = euclidean(x,y)

    triangle_area = area(edge_length)

    circumcircle_radius = circumcircle(x,y)

    #print("circumcircle_radius: {0[0]}:{1[0]},{0[1]}:{1[1]}, {0[2]}:{1[2]} \n {2}".format(x,y,circumcircle_radius))
    # 5. calculat the cetral angle and their gcd
    angle = centerAngle(edge_length, circumcircle_radius)
    
    gcd_angle = gcd(gcd(angle[0], angle[1]), angle[2])


    result = 2 * math.pi / gcd_angle * circumcircle_radius * math.sin(gcd_angle) * circumcircle_radius * 0.5 
    if DEBUG:
        print("circumcircle_radius",circumcircle_radius)
        print("totoal_angle",angle)
        print("gcd_angle",gcd_angle)
        print("len",edge_length)
    print("{:.8f}".format(result))
    
    



if __name__ == "__main__":
    main()
