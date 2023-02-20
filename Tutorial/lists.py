

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
lucky_number = [4, 8, 15, 16, 23, 42]

#slicing: cat nho list
#has format: [start : end : step]
#print(friends[0])

#in tu 1(ko in 0)
#print(friends[1:])

#print(friends[1:3]): cat tu 1-2(khong co index 3)

#truy cap den phan tu co vi tri cuoi cung:
#print(friends[-1])

#step: buoc nhay
#neu step == -1: vd: <list>[::-1]: reverse list

#List functions

#tra ve do dai List: len()
#tra ve index: index(ptu_list)
#them phan tu vao list: insert(index, ptu), append, extend
#xoa: remove(ptu)(xoa gia tri dau tien cua ptu nhap vao), clear, pop(ptu), del <list>[index]
#dem so lan xuat hien: count
#sap xep: sort, sorted
#sx giam dan: <list>.sort(reverse = True)
#sorted: sap xep khong anh huong den <list> cu (hay sorted tao 1 list moi: tuong tu co reversed)
#dao list: reverse
#tao ban sao: copy
#tra ve phan tu max trong list: max(<list>) (tuong tu: min)
#tong list: sum(<list>)
#zip

#enumerate: cho phep tra ve index, gia tri trong list
for index, friend in enumerate(friends):
    print(f"Friend #{index}: {friend}")
#index bat dau tu 0. Muon index bat dau in ra tu 1 so bat ky:
for index, friend in enumerate(friends, start = 1):
    print(f"Friend #{index}: {friend}")