
class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def __str__(self):
        a = abs(self.thuc)
        b = abs(self.ao)
        if(self.ao > 0):
            return f"{self.thuc} + {self.ao}i"
        else:
            return f"{self.thuc} - {b}i"

def cong(sp1: SoPhuc, sp2: SoPhuc):
    a = sp1.thuc + sp2.thuc
    b = sp1.ao + sp2.ao
    return SoPhuc(a, b)

def nhan(sp1: SoPhuc, sp2: SoPhuc):
    a = sp1.thuc * sp2.thuc - sp1.ao * sp2.ao
    b = sp1.ao * sp2.thuc + sp2.ao * sp1.thuc
    return SoPhuc(a, b)

if __name__ == "__main__":
    for _ in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        sp1 = SoPhuc(x1, y1)
        sp2 = SoPhuc(x2, y2)
        tmp = cong(sp1, sp2)
        res1 = nhan(sp1, tmp)
        res2 = nhan(tmp, tmp)
        print(res1, ", ", res2, sep="")