class Gamer :
    def __init__(self, id, ten, gV, gR):
        self.id = id
        self.ten = ten
        self.thoiGian = gR[0] * 60 + gR[1] - gV[0] * 60 - gV[1]

    def __str__(self) -> str:
        return f"{self.id} {self.ten} {self.thoiGian // 60} gio {self.thoiGian % 60} phut"

n = int(input())
l = []
for _ in range(n):
    id = input()
    ten = input()
    gV = [int(i) for i in input().split(':')] 
    gR = [int(i) for i in input().split(':')]
    l.append(Gamer(id, ten, gV, gR))
l = sorted(l, key= lambda el : -el.thoiGian)
print(*l, sep= '\n')

