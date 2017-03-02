#!/usr/bin/python3
# _*_ coding:utf-8 _*_

def main():
    a = int(input())
    for i in range(a):
        b=input()
        if len(b) <= 10:
            print(b)
        else:
            print(b[0]+str(len(b)-2)+b[len(b)-1])


def main2():
    b=int(input())
    for i in range(b):
        b=input()
        print(b if len(b) < 11 else b[0]+str(len(b)-2)+b[len(b)-1])




if __name__ == "__main__":
    #main()
    main2()
