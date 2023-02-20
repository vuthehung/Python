if __name__ == '__main__':
    t=int(input())
    while(t>0):
        s=input().split()
        dem=0
        for i in s:
            dem+=len(i)
            if(dem<100):
                print(i,end=' ')
                dem+=1
            else:
                break
        print()
        t-=1