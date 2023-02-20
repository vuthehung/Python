
def thuannghich(s):
    tmp = s[::-1]
    return tmp == s


file = open('VANBAN.in', 'r')
lines = file.readlines()

l = []
for i in lines:
    l.extend(i.split())

d = dict()

for i in l:
    if thuannghich(i):
        d[i] = l.count(i)

d_s = dict(sorted(d.items(), key= lambda el : 1000 - len(el[0])))

x = list(d_s.keys())
max_l = len(x[0])

for i in d.items():
    if len(i[0]) == max_l:
        print(f"{i[0]} {i[1]}")
