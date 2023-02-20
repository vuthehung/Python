def cunghoangdao(ngay, thang):
    if ngay >= 21 and thang == 3 or ngay <= 19 and thang == 4:
        print("Bach Duong")
    elif ngay >= 20 and thang == 4 or ngay <= 20 and thang == 5:
        print("Kim Nguu")
    elif ngay >= 21 and thang == 5 or ngay <= 20 and thang == 6:
        print("Song Tu")
    elif ngay >= 21 and thang == 6 or ngay <= 22 and thang == 7:
        print("Cu Giai")
    elif ngay >= 23 and thang == 7 or ngay <= 22 and thang == 8:
        print("Su Tu")
    elif ngay >= 23 and thang == 8 or ngay <= 22 and thang == 9:
        print("Xu Nu")
    elif ngay >= 23 and thang == 9 or ngay <= 22 and thang == 10:
        print("Thien Binh")
    elif ngay >= 23 and thang == 10 or ngay <= 22 and thang == 11:
        print("Thien Yet")
    elif ngay >= 23 and thang == 11 or ngay <= 21 and thang == 12:
        print("Nhan Ma")
    elif ngay >= 22 and thang == 12 or ngay <= 19 and thang == 1:
        print("Ma Ket")
    elif ngay >= 20 and thang == 1 or ngay <= 18 and thang == 2:
        print("Bao Binh")
    elif ngay >= 19 and thang == 2 or ngay <= 20 and thang == 3:
        print("Song Ngu")


def solve():
    t = int(input())
    for _ in range(t):
        d, m = map(int, input().split())
        cunghoangdao(d, m)



def main():
    solve()

if __name__ == "__main__":
    main()