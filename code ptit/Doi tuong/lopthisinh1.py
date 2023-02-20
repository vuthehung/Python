

class ThiSinh():
    def __init__(self, name, dob, score1, score2, score3):
        self.name = name
        self.dob = dob
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def __str__(self):
        return "{} {} {}".format(self.name, self.dob, "%.1f"%(self.score1 + self.score2 + self.score3))

a = []
for _ in range(5):
    a.append(input())

for i in range(2, 5):
    a[i] = float(a[i])

ts = ThiSinh(a[0], a[1], a[2], a[3], a[4])
print(ts)

