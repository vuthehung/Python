import math

class PhanSo():
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutgon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu = self.tu / ucln
        self.mau = self.mau / ucln

    def __str__(self):
        return f"{int(self.tu)}/{int(self.mau)}"

if __name__ == "__main__":
    tu, mau = map(int, input().split())
    ps = PhanSo(tu, mau)
    ps.rutgon()
    print(ps)