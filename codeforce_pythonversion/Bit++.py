#!/usr/bin/python3
# _*_ coding:utf-8 _*_

__author__ = 'zhangxun'


def main():
    result = 0
    for i in range(int(input())):
        action = input()
        if action[0] in ["+","-"]:
            if action[0] == "+":
                result += 1
            else:
                result -= 1
        else:
            if action[-1] == "+":
                result += 1
            else:
                result -= 1

    print(result)


def main_one_line_try():
    print()


if __name__ == '__main__':
    main()