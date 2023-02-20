def xuly(s):
    s1 = s.lower()
    tmp = s1.split('@')
    return tmp[0] + '@' + tmp[1]


file = open('CONTACT.in', 'r')
lines = file.readlines()
l = []
for i in lines:
    l.append(i.split('\n')[0])
s = set()
for i in l:
    s.add(xuly(i))

res = list(s)
res.sort()
for i in res:
    print(i)


