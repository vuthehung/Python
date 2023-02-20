

class HoaDon:
    def __init__(self, i, ten, soC, soM):
        self.id = 'KH' + '{:02d}'.format(i)
        self.ten = ten
        self.soC = soC
        self.soM = soM
        phuPhi = None
        tienNuoc = None
        dT = soM - soC
        if(dT >= 0 and dT <= 50):
            phuPhi = 2 / 100
            tienNuoc = dT * 100
        elif (dT >= 51 and dT <= 100):
            phuPhi = 3 / 100
            tienNuoc = 50 * 100 + (dT - 50) * 150
        else:
            phuPhi = 5 / 100
            tienNuoc = 50 * 100 + 50 * 150 + (dT - 100) * 200
        
        self.thanhTien = tienNuoc + tienNuoc * phuPhi
    
    def __str__(self) -> str:
        return f"{self.id} {self.ten} {round(self.thanhTien)}"

n = int(input())
l = []
for i in range(n):
    l.append(HoaDon(i + 1, input(), int(input()), int(input())))

l = sorted(l, key= lambda el : -el.thanhTien)
print(*l, sep= '\n')

