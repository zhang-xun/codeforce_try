#!/usr/bin/python3
# _*_ coding:utf-8 _*_


def main():
    input()
    input_string = input()
    flag = ""
    max_count = 0
    for i in input_string:
        if i == flag:
            max_count += 1
        else:
            flag = i

    #print([input_string[i]==input_string[i-1] for i in range(1,len(input_string))])
    print(max_count)


def main_from_codeforce():
    input()
    s = input()
    print(sum([s[i] == s[i - 1] for i in range(1, len(s))]))


if __name__ == '__main__':

    main()