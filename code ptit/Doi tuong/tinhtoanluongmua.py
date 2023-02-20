def time(start,end):
    return end[0]-start[0]+(end[1]-start[1])/60
        
if __name__ == '__main__':
    n=int(input())
    data={}
    for i in range(n):
        tram=input()
        start=[int(x) for x in input().split(":")]
        end=[int(x) for x in input().split(":")]
        luongmua=float(input())
        if(tram in data):
            data[tram][0]+=time(start,end)
            data[tram][1]+=luongmua
        else:
            data[tram]=[time(start,end),luongmua]
    dem=1
    for i in data.items():
        print("T{:0>2} {} {:.2f}".format(dem,i[0],i[1][1]/i[1][0]))
        dem+=1
        
