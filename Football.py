#!/usr/bin/python3
# _*_ coding:utf-8 _*_


def main():
    football_player = input()
    # print(["NO","YES"][ i for i in football_player if ])
    max_couter, couter, flag = 0, 0, football_player[0]
    for i in football_player:
        if i == flag:
            couter += 1
        else:
            flag = i
            if couter > max_couter:
                max_couter = couter
            couter = 1
    if couter > max_couter:
        max_couter = couter
    print(["NO", "YES"][max_couter >= 7])


def main_from_cf1():
    football_player  = input()
    if "1111111" in  football_player or "0000000" in football_player:
        print("YES")
    else:
        print("NO")

def main_from_cf_oneline():
    football_player = input()
    print(["NO","YES"]["0"*7 in football_player or "1"*7 in football_player])


if __name__ == '__main__':
    main_from_cf_oneline()
    main()
