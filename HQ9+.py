#!/usr/bin/python3
# _*_ coding:utf-8 _*_


def main():
    s = input()
    print(["YES","NO"][sum(i for i in s if i in ["H","Q","9","+"]) >= 1 ])

if __name__ == '__main__':
    main()