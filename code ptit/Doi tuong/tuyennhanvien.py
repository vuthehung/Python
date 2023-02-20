class NhanVien :
    def __init__(self, id, ten, d1, d2) :
        self.id = 'TS0' + str(id) 
        self.ten = ten
        if d1 > 10: d1 = d1 / 10
        if d2 > 10: d2 = d2 / 10

        self.dTB = (d1 + d2) / 2
        if self.dTB < 5:
            self.xL = 'TRUOT'
        elif self.dTB >= 5 and self.dTB < 8:
            self.xL = 'CAN NHAC'
        elif self.dTB >= 8 and self.dTB < 9.5:
            self.xL = 'DAT'
        else:
            self.xL = 'XUAT SAC'

    def __str__(self) -> str:
        return f"{self.id} {self.ten} {'{:.2f}'.format(self.dTB)} {self.xL}"
    
n = int(input())
l = []

for i in range(n):
    ten = input()
    d1 = float(input())
    d2 = float(input())
    l.append(NhanVien(i + 1, ten, d1, d2))

l = sorted(l, key= lambda el : -el.dTB)
print(*l, sep= '\n')

