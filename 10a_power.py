def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    n,p1,p2,p3,t1,t2 = [int(i) for i in input().split()]
    timeperiods = []
    result = 0
    for i in range(n):
        timeperiods.append([int(i) for i in input().split()])
    for i in range(len(timeperiods)):
        result += (timeperiods[i][1]-timeperiods[i][0])*p1
    for i in range(len(timeperiods)-1):
        betweenT = abs(timeperiods[i+1][0]-timeperiods[i][1])
        if betweenT <= t1:
            result += betweenT *p1
        elif betweenT <= t1+t2:
            result += t1*p1 +(betweenT - t1)*p2
        else:
            result += t1*p1+t2*p2 + (betweenT-t1-t2)*p3
    print(result)

if __name__ == "__main__":
    main()
