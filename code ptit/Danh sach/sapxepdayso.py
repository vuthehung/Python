if __name__ == '__main__':
    t=int(input())
    while(t>0):
        n, m = map(int, input().split())
        a = [int(x) for x in input().split()]
        mx = max(a)
        check = True
        duong = ""
        for i in a:
            if(i == mx and check):
                duong+=str(m)+" "+str(i)+" "
                check = False
            elif(i < 0):
                print(i , end=' ')
            else:
                duong += str(i) + " "
        print(duong)
        t-=1
