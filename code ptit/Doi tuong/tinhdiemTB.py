class SV:
    def __init__(self, id, ten, d1, d2, d3):
        self.id = 'SV{:02d}'.format(id)
        self.ten = ten
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.dTB = round((d1 * 3 + d2 * 3 + d3 * 2) / 8 + 0.001, 2)
        self.xH = None

    def __str__(self) -> str:
        return f'{self.id} {self.ten} {"{:.2f}".format(self.dTB)} {self.xH}'


def chuanHoa(s: str) -> str:
    tmp = s.lower().strip().split()
    return ' '.join(tmp).title()

n = int(input())
a = []
for i in range(n):
    ten = chuanHoa(input())
    d1 = float(input())
    d2 = float(input())
    d3 = float(input())
    a.append(SV(i + 1, ten, d1, d2, d3))

a.sort(key= lambda el : el.ten)
a.sort(key= lambda el : -el.dTB)

xH = 1
cnt = 0
a[0].xH = 1

for i in range(1, n):
    if a[i - 1].dTB == a[i].dTB:
        a[i].xH = xH
        cnt += 1
    else:
        xH += cnt + 1
        a[i].xH = xH
        cnt = 0

print(*a, sep= '\n')

# 2
#  ha Thi kieu     anh
# 7
# 6
# 7
# Pham    THI  HAO
# 6
# 7
# 6
