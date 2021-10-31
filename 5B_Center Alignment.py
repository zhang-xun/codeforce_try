def main():
    temp = []
    while 1:
        try:
            temp.append(input())
        except:
            break
    max_index,c = max([len(i) for i in temp]), 0
    print("*"*(max_index+2))
    for i in temp:
        s = [(max_index-len(i))/2]*2
        if len(i)%2 != max_index %2:
            c = 1-c
            s[c] += 1
        print("*"+" "*int(s[0])+i+" "*int(s[1]) +"*")    
    print("*"*(max_index+2))

if __name__ == "__main__":
    main()
    '''
************
* This  is *
*          *
*Codeforces*
*   Beta   *
*  Round   *
*     5    *
************ 

************
* This  is *
*          *
*Codeforces*
*   Beta   *
*  Round   *
*    5     *
************
****************
*welcome to the*
*  Codeforces  *
*     Beta     *
*   Round 5    *
*              *
*      and     *
*  good luck   *
****************
'''