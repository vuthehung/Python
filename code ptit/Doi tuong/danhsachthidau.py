
class Team:
    def __init__(self, maT, info):
        self.maT = maT
        self.info = info

class TS(Team):
    def __init__(self, maTS, ten, maT, info):
        super().__init__(maT, info)
        self.maTS = 'C{:03d}'.format(maTS)
        self.ten = ten

    def __str__(self) -> str:
        return f'{self.maTS} {self.ten} {self.info[0]} {self.info[1]}'

n = int(input())
team = {}
for i in range(n):
    maT = 'Team{:02d}'.format(i + 1)
    tenT = input()
    tenTr = input()
    team[maT] = [tenT, tenTr]

m = int(input())
a = []
for i in range(m):
    ten = input()
    maT = input()
    info = team[maT]
    a.append(TS(i + 1, ten, maT, info))

a.sort(key= lambda el : el.ten)
print(*a, sep= '\n')

