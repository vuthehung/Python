
class TL:
    def __init__(self, idTL, tenTL):
        self.idTL = idTL
        self.tenTL = tenTL

class Phim(TL):
    def __init__(self, idP, idTL, tenTL, ngay, tenP, soT):
        super().__init__(idTL, tenTL)
        self.idP = 'P' + '{:03d}'.format(idP)
        self.ngay = ngay.split('/')
        self.tenP = tenP
        self.soT = soT
    
    def __str__(self) -> str:
        return f'{self.idP} {self.tenTL} {"/".join(self.ngay)} {self.tenP} {self.soT}'

n, m = map(int, input().split())
d = {}
l = []
for i in range(n):
    idTL = 'TL' + '{:03d}'.format(i + 1)
    d[idTL] = input()
for i in range(m):
    idTL = input()
    ngay = input()
    tenP = input()
    soT = int(input())
    l.append(Phim(i + 1, idTL, d[idTL], ngay, tenP, soT))

l.sort(key= lambda el : (-el.soT, el.tenP))
l.sort(key= lambda el : int(el.ngay[2] + el.ngay[1] + el.ngay[0]))
print(*l, sep= '\n')

