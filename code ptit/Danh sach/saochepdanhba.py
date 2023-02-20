
def cmp(l):
    t = l[0].split()
    return t[-1]

def cmp2(l):
    t = l[0].split()
    return t[len(t) - 2]

def solve():
    file = open('SOTAY.txt', 'r')
    inp = []
    for line in file:
        inp.extend(line.strip().split('\n'))
    i = 0
    day = ''
    data = []
    while(i < len(inp)):
        if inp[i].find('Ngay') != -1:
            day = inp[i][5::]
        else:
            data.append([inp[i], inp[i + 1], day])
            i += 1
        i += 1
    data.sort(key= cmp)
    data.sort(key= cmp2)
    for i in data:
        print(f"{i[0]}: {i[1]} {i[2]}")
    file.close()

if __name__ == '__main__':
    solve()

# def cmp(x):
#     x=x[0].split()
#     return x[len(x)-1]
# def cmp2(x):
#     x=x[0].split()
#     return x[len(x)-2]

# if __name__ == '__main__':
#     f1=open("D:\code\codePython\code ptit\Danh sach\\test.in","r")
#     oldday=""
#     data_raw=f1.read().strip().split("\n")
#     data=[]
#     i=0 
#     while(i<len(data_raw)):
#         if(data_raw[i].find("Ngay")!=-1):
#             oldday=data_raw[i][5::]
#         else:
#             data.append([data_raw[i],data_raw[i+1],oldday])
#             i+=1
#         i+=1
#     data.sort(key=cmp2)
#     data.sort(key=cmp)
#     for i in data:
#         print("{}: {} {}".format(i[0],i[1],i[2]))
#     f1.close()