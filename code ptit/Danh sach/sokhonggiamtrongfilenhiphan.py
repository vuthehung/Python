

def soKG(n):
    if(n < 10):
        return False
    k = 10
    while(n > 0):
        if(n % 10 > k):
            return False
        k = n % 10
        n /= 10
    
    return True
    
f1 = open('DATA1.in', 'rb')
f2 = open('DATA2.in', 'rb')

num1 = list(f1.read())
num2 = list(f2.read())

res = set(num1)

d1 = {}

for i in res:
    if soKG(i) and (i in num2):
        d1[i] = [num1.count(i), num2.count(i)]

d1 = dict(sorted(d1.items(), key= lambda el : el[0]))

for i in d1.items():
    print(i[0], i[1][0], i[1][1])




