import math

def object(tu, mau):
    return PhanSo(tu, mau)

class PhanSo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def rutgon(self):
        ucln = int(math.gcd(self.x, self.y))
        self.x = self.x // ucln
        self.y =  self.y // ucln

    def cong(self, PhanSo):
        mau = self.y * PhanSo.y
        tu = self.x * PhanSo.y + PhanSo.x * self.y
        return object(tu, mau)

    def __str__(self):
        return f"{self.x}/{self.y}"

if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input().split())
    ps1 = PhanSo(x1, y1)
    ps2 = PhanSo(x2, y2)
    res = ps1.cong(ps2)
    res.rutgon()
    print(res)