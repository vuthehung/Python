def solve():
    file = open('D:\code\codePython\code ptit\Danh sach\DATA1.in', 'r')
    l = []
    for i in range(int(file.readline())):
        ma = 'C' + "{:03d}".format(i + 1)
        l.append([ma, file.readline().strip(), file.readline().strip(), file.readline().strip()])
    res = sorted(l, key=lambda el: (el[2], el[0]))
    for i in res:
        print(*i)
if __name__ == "__main__":
    solve()

# 2
# 09/01/2022
# 15:30
# 70172
# 09/01/2022
# 10:00
# 70279

# from datetime import datetime
# class ca:
#     def __init__(self, i, date, time, room) -> None:
#         self.code = 'C' + str(i).zfill(3)
#         self.date = date
#         self.time = time
#         self.room = room
#         self.dtime = datetime.strptime(date + ' ' + time, '%d/%m/%Y %H:%M')
#     def __str__(self) -> str:
#         return self.code + ' ' + self.date + ' ' + self.time + ' ' + self.room
# a = []
# f = open('CATHI.in')
# for i in range(int(f.readline())): a.append(ca(i+1, f.readline().strip(), f.readline().strip(), f.readline().strip()))
# a.sort(key=lambda x: (x.dtime, x.code))
# for i in a: print(i)