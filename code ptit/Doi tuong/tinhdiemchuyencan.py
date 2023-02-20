# t = int(input())
# m = {}
# for i in range(t) :
#     maSV = input()
#     ten = input()
#     lop = input()
#     m[maSV] = [ten, lop]
# for i in range(t) :
#     maSV, cc = input().split()
#     d = 10
#     for j in cc :
#         if j == 'm' : d -= 1
#         elif j == 'v' : d -= 2
#     if d < 0 : d = 0
#     m[maSV] = m[maSV] + [d]
# for i in m :
#     print(i, end = ' ')
#     for j in m[i] :
#         print(j, end = ' ')
#     if(m[i][-1] == 0) : print('KDDK')
#     else : print()

class SV:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten 
        self.lop = lop
        self.dCC = 0
        self.ghiC = ''

    def __str__(self) -> str:
        return f"{self.ma} {self.ten} {self.lop} {self.dCC} {self.ghiC}"

def tinhDCC(s: str) -> int:
    d = 10
    for i in s:
        if i == 'm':
            d -= 1
        elif i == 'v':
            d -= 2
    if d < 0: d = 0
    return d

n = int(input())
a = []
for i in range(n):
    a.append(SV(input(), input(), input()))

d = {}
for i in range(n):
    ma, cc = input().split()
    d[ma] = cc

for i in a:
    i.dCC = tinhDCC(d[i.ma])
    if i.dCC == 0:
        i.ghiC = 'KDDK'    

print(*a, sep= '\n')

# 3
# B19DCCN999
# Le Cong Minh
# D19CQAT02-B
# B19DCCN998
# Tran Truong Giang
# D19CQAT02-B
# B19DCCN997
# Nguyen Tuan Anh
# D19CQCN04-B
# B19DCCN998 xxxmxmmvmx
# B19DCCN997 xmxmxxxvxx
# B19DCCN999 xvxmxmmvvm