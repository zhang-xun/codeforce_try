#!/usr/bin/python3
# _*_ coding:utf-8 _*_

__author__ = 'zhangxun'

def main():
    couter = 0
    for i in range(int(input())):
        sure_solution = input().split()
        if(eval("+".join(sure_solution)) >= 2):
            couter += 1

    print(couter)




if __name__ == '__main__':
    main()