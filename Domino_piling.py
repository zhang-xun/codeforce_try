#!/usr/bin/python3
# _*_ coding:utf-8 _*_


__author__ = 'zhangxun'


def main():
    m_n_scale = input()
    m = int(m_n_scale.split(" ")[0])
    n = int(m_n_scale.split(" ")[1])
    couter = 0
    if m == 1:
        couter += n // 2
    elif m >= 2 and m % 2 == 0:
        couter += (m // 2) * n
    else:
        couter += (m // 2) * n
        couter += n // 2


    print(couter)


def main_from_codeforce():
    print(eval('*'.join(input().split()))//2)



if __name__ == '__main__':
    print('*'.join(input().split()))
    print(eval("*".join(input().split())))
    main()