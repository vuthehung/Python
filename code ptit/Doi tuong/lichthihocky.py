
class MonHoc:
    def __init__(self, maM, tenM):
        self.maM = maM
        self.tenM = tenM

class LichThi(MonHoc):
    def __init__(self, id, maM, tenM, ngay, gio, nhom):
        super().__init__(maM, tenM)
        self.id = 'T{:03d}'.format(id)
        self.ngay = ngay.split('/')
        self.gio = gio.split(':')
        self.nhom = nhom

    def __str__(self) -> str:
        return f'{self.id} {self.maM} {self.tenM} {"/".join(self.ngay)} {":".join(self.gio)} {self.nhom}'

n,m = map(int, input().split())
mH = {}
a = []
for i in range(n):
    maM = input()
    tenM = input()
    mH[maM] = tenM

for i in range(m):
    tmp = input().split()
    maM = tmp[0]
    tenM = mH[maM]
    ngay = tmp[1]
    gio = tmp[2]
    nhom = tmp[3]
    a.append(LichThi(i + 1, maM, tenM, ngay, gio, nhom))

a.sort(key= lambda el : el.maM)
a.sort(key= lambda el : int(el.gio[0] + el.gio[1]))
a.sort(key= lambda el : int(el.ngay[2] + el.ngay[1] + el.ngay[0]))

print(*a, sep= '\n')

