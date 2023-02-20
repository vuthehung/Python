def func1(n):
    return n[0]
def func2(n):
    return n[1]
def func3(n):
    return n[2]

n = int(input())
a = []
for _ in range(n):
    tmp = []
    tmp.append(input())
    ac, sub = map(int, input().split())
    tmp.append(ac)
    tmp.append(sub)
    a.append(tmp)

a.sort(key= func1)
a.sort(key= func3)
a.sort(reverse= True, key= func2)
for i in a:
    print(i[0], i[1], i[2])