
#list_comprehensions: new_list[<action> for <item> in <iterator> if <some condition>]

# word = "Hello World"
# print([char for char in word]) #['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

# even_numbers = [i for i in range(0, 10) if i % 2 == 0] #list chua ca so chan tu 0 den 9

#hoac co the su dung ham lam action

#zip(): lap 2 list cung 1 luc:
# wizards = ["Harry Potter", "Ron", 'Hermione']
# pets = ["Hedwig", "Scabber", 'Crookshank']
# for wiz, pet in zip(wizards, pets):
#     print(f"{wiz} has {pet}")

#sorted: nang cao
# sorted_by_first = sorted(['hi', 'hello', 'you', 'A']) #mac dinh sap xep theo chu cai dau
# sorted_by_second = sorted(['hi', 'hello', 'you', 'A'], key=lambda el: el[1])# el tuong ung voi 1 ptu trong list
# print(sorted_by_first)
# print(sorted_by_second)

#mang 2 chieu: 2D_list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# for row in number_grid:
#     print(row)
#     for colum in row:
#         print(colum)

#transform Matrix in List: used list comprehensions
list_converted = [number_grid[row][col] for row in range(len(number_grid)) for col in range(len(number_grid))]
print(list_converted)

#combine colums with zip and *: gop cac cot
print([x for x in zip(*number_grid)])