from datetime import datetime

tien = [0, 25, 34, 50, 80]
class HoaDon:
    def __init__(self, id, ten, phong, ngayN, ngayT, tienDV):
        self.id = 'KH{:02d}'.format(id)
        self.ten = ten
        self.phong = phong
        self.soNgayO = str(datetime.strptime(ngayT, '%d/%m/%Y') - datetime.strptime(ngayN, '%d/%m/%Y')).split()[0]
        if self.soNgayO == '0:00:00': self.soNgayO = 1
        else: self.soNgayO = int(self.soNgayO) + 1

        self.tienPhong = tien[int(self.phong[0])] * self.soNgayO + tienDV

    def __str__(self) -> str:
         return f'{self.id} {self.ten} {self.phong} {str(self.soNgayO)} {str(self.tienPhong)}'

n = int(input())
a = []
for i in range(n):
    a.append(HoaDon(i + 1, input(), input(), input().strip(), input().strip(), int(input())))

a.sort(key= lambda el : -el.tienPhong)
print(*a, sep= '\n')

# 3
# Huynh Van Thanh   
# 103 
# 05/06/2010   
# 05/06/2010   
# 15
# Le Duc Cong  
# 106 
# 08/03/2010   
# 01/05/2010   
# 220
# Tran Thi Bich Tuyen   
# 207 
# 10/04/2010   
# 21/04/2010   
# 96