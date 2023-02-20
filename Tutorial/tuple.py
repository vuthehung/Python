#khac list la: tuple khong the thay doi gia tri trong tuple
#ktao tuple: t = ()
coordinates = (4, (5, 6))
#coordinates[0] = 1 #error: vi tuple ko thay doi duoc
print(coordinates[1][0])