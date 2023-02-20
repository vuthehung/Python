
mon = ['TOAN', 'LY', 'HOA']
uT = [0, 2, 1.5, 1, 0]
class GV:
    def __init__(self, id, ten, maXT, d1, d2):
        self.id = 'GV' + '{:02d}'.format(id)
        self.ten = ten
        self.monXT = mon[ord(maXT[0]) - ord('A')]
        self.diemXT = d1 * 2 + d2 + uT[int(maXT[1])]
        if self.diemXT >= 18:
            self.status = 'TRUNG TUYEN'
        else:
            self.status = 'LOAI'
    def __str__(self) -> str:
        return f"{self.id} {self.ten} {self.monXT} {'{:.1f}'.format(self.diemXT)} {self.status}"

n = int(input())
l = []

for i in range(n):
    l.append(GV(i + 1, input(), input(), float(input()), float(input())))

l.sort(key= lambda el : -el.diemXT)
print(*l, sep= '\n')

