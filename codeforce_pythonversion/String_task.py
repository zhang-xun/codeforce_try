#!/usr/bin/python3
# _*_ coding:utf-8 _*_
import math


def deleteDuplicateElement(list_todelete):
    result = []
    for item in list_todelete:
        if len(result) > 0:
            if item  == "." and result[-1] == ".":
                pass
            elif  abs(ord(item) - ord(result[-1])) <= abs(ord("z") - ord("a")):
                result.append(".")
                result.append(item)
            else:
                result.append(item)
        else:
            result.append(item)
    if result[0] != ".":
        result.insert(0,".")
    return result

def translate_dot(list_tobemodify):
    vowels = ["a", "A", "O", "o", "Y", "y", "e", "E", "U", "u", "I", "i"]
    result = []
    for i in list_tobemodify:
        if i in vowels:
            result.append(".")
        else:
            result.append(i.lower())
    return  result


def main():
    test_string = input()
    result = translate_dot(test_string)
    # handle the last element
    result2 = (deleteDuplicateElement(result))
    if result2[-1] == ".":
        result2.pop()
    print("".join(result2))


def main2_from_codeforce():
    while True:
        print("".join("." + l for l in input().lower() if l not in 'aeiouy'))

if __name__ == '__main__':
    main2_from_codeforce()
    main()



