#! /usr/bin/python3
# _*_ coding:utf-8 _*_

def main():
    a = input()
    if int(a) % 2 != 0 or int(a) == 2:
        print("NO")
        return
    for i in range(1,int(int(a) / 2)):
        #print(i*2)
        if (int(a) - i*2) % 2 == 0 and int(a) - i*2 != 0:
            print("YES")
            break
        else:
            print("NO")
            break


if __name__ == "__main__":
    #main()
    print(int(False),int(True))
    print("YNEOS"[2 ** int(input()) % 24 < 9::2])
    n=int(input())
    print(["NO","YES"][  n % 2 == 0 and n > 2 ])
    print([ n % 2 == 0 and n > 2])
    print([1,2,3][False])
