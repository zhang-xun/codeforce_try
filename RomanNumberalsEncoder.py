#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_


def solution(n):
    transform = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
    #print(type(transform))
    result = []
    for i in sorted(transform.keys(),reverse=True):
        while(n > 0):
            if n >= i:
                x,n = divmod(n,i)
                result.append(x*transform[i])
                #Rprint("x:n:i",x,n,i)
            else:
                #print("i,x,n",i,x,n)
                break

    return "".join(result)


if __name__ == '__main__':
    print(solution(1990))
    print(solution(1490))
    print(solution(4))
    print(solution(6))
    print(solution(1990))
    print(solution(1666))