
f1 = open('D:\code\codePython\code ptit\Danh sach\DATA1.in', 'r')
f2 = open('D:\code\codePython\code ptit\Danh sach\DATA2.in', 'r')
f3 = open('D:\code\codePython\code ptit\Danh sach\DATA3.in', 'r')

class LichThi:
    def __init__(self, maCa, ngay, gio, phong, tenMon, nhom, soL):
        self.maCa = maCa
        self.ngay = ngay.split('/')
        self.gio = gio.split(':')
        self.phong = phong
        self.tenMon = tenMon
        self.nhom = nhom
        self.soL = soL

    def __str__(self) -> str:
        return f"{'/'.join(self.ngay)} {':'.join(self.gio)} {self.phong} {self.tenMon} {self.nhom} {self.soL}"

monThi = {}
caThi = {}

for i in range(int(f1.readline())):
    maM = f1.readline().strip()
    tenM = f1.readline().strip()
    hTT = f1.readline().strip()
    monThi[maM] = [tenM, hTT]

for i in range(int(f2.readline())):
    maC = 'C{:03d}'.format(i + 1)
    ngay = f2.readline().strip()
    gio = f2.readline().strip()
    phong = f2.readline().strip()
    caThi[maC] = [ngay, gio, phong]

lichThi = []

for i in range(int(f3.readline())):
    info = f3.readline().split()
    infoCa = caThi[info[0]]
    ngay = infoCa[0]
    gio = infoCa[1]
    phong = infoCa[2]
    infoMonThi = monThi[info[1]]
    tenM = infoMonThi[0]
    nhom = info[2]
    soL = info[3]
    lichThi.append(LichThi(info[0], ngay, gio, phong, tenM, nhom, soL))

lichThi.sort(key= lambda el : el.maCa)
lichThi.sort(key= lambda el : int(el.gio[0] + el.gio[1]))
lichThi.sort(key= lambda el : int(el.ngay[2] + el.ngay[1] + el.ngay[0]))

print(*lichThi, sep= '\n')
