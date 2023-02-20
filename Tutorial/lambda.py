#Ham an danh - Lambda
#cu phap: lambda arguments: expression

#define: dinh nghia ham lambda
# code = lambda so: so + 69
#tuong duong voi ham sau:
# def code1(so):
#     return so + 69
#print(code(1)) # 1 + 69 = 70
# codeXplore = lambda x, y, z : x + y - z
# print(codeXplore(6, 9, 10))

#custom sorting using a lambda function as key parameter

# coordinate2D = [(6, 9), (9, 6), (-1, 3), (2, 10)]
# print(sorted(coordinate2D)) #sap xep theo gia tri thu nhat cua moi cap
# #sap xep theo gia tri thu hai cua cac cap
# print(sorted(coordinate2D, key= lambda point: point[1]))

# number_list = [5, 3, -2, 4, 1, -1, -3, 4, 5]
# #sort theo tri tuyet doi
# print(sorted(number_list, key= lambda x : abs(x)))

#map
# list_keyword = ["codexplore", "welcome", "cac ban"]
# print(list(map(lambda x: x.title(), list_keyword)))

# #filter(function, seq)
# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda x: x % 2 != 0, number_list)))
# #tuong tu list_comprehension
# new_list = [x for x in number_list if x % 2 != 0]
# print(new_list)

#reduce(function, seq): function: phai co 2 bien
from functools import reduce
sequence = [1, 3, 5, 9, 6, 2, 8]
# print(reduce(lambda a, b: a + b, sequence))
print(reduce(lambda a, b: a if a > b else b, sequence))#tim max