class BangDiem:
    def __init__(self):
        self.stt=0
        self.ten=""
        self.diem=[]
        self.tb=0
        self.xeploai=""
    def read(self):
        self.ten=input()
        self.diem=[float(x) for x in input().split()]
    def setSTT(self,n):
        self.stt=n
    def getTB(self):
        return self.tb
    def calc(self):
        self.tb+=self.diem[0]*2
        self.tb+=self.diem[1]*2
        for i in range(2,10):
           self.tb+=self.diem[i]
        self.tb=round(self.tb/12+0.01,1)
        if(self.tb>=9):
            self.xeploai="XUAT SAC"
        elif(self.tb>=8):
            self.xeploai="GIOI"
        elif(self.tb>=7):
            self.xeploai="KHA"
        elif(self.tb>=5):
            self.xeploai="TB"
        else:
            self.xeploai="YEU"
    def info(self):
        print("HS{:0>2} {} {:.1f} {}".format(self.stt,self.ten,self.tb,self.xeploai))
        
if __name__ == '__main__':
    n=int(input())
    data=[]
    for i in range(n):
        info=BangDiem()
        info.setSTT(i+1)
        info.read()
        info.calc()
        data.append(info)
    data.sort(reverse=True,key=lambda x:x.getTB())
    for i in data:
        i.info()