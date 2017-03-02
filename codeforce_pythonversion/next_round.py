#!/usr/bin/python3
# _*_ coding:utf-8 _*_

def main():
    #read first parameter
    number_and_score = input()
    #number_of_players= number_and_score.split(" ")[0]
    index = number_and_score.split(" ")[1]

    #read second parameters
    person_score = input().split(" ")

    #update the score
    max_score = person_score[int(index)-1]

    cout = 0
    for i in person_score:
        if int(max_score) <= int(i) and int(i):
            cout += 1

    print(cout)

if __name__ == '__main__':
    main()