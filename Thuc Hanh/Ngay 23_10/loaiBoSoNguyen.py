file = open("DATA.in", "r")
lines = file.readlines()
a = []
res = []
num = []
for i in lines:
    tmp = list(i.split())
    a.extend(tmp)
for i in a:
    try:
        x = int(i)
        num.append(x)
    except ValueError:
        res.append(i)
for i in num:
    if i > 10 ** 9:
        s = str(i)
        res.append(s)
res.sort()
print(*res)
