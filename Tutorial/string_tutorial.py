

phrase = "Vu The Hung"
'''
#chu thuong
print(phrase.lower())
#chu hoa
print(phrase.upper())
#do dai str
print(len(phrase))
#tra ve vi tri
print(phrase.index("H"))
#thay the 1 tu(cum tu(ky tu))
print(phrase.replace("H", "h"))
'''
#escaping backslash: \
#ta co the dung ca '' va "" de bieu dien string
#gan 1 string vua co '' va "" thi dung \
my_string = "I'm living \"Ha Noi\""

#string is immutable -> cannot be changed
#eg: my_string[0] = "M": error

#substring with slicing
#stringName[startIndex:endIndex]
#neu substring co index cuoi la index cuoi cua string thi bo trong endIndex(tuong tu index dau)
sub_string = my_string[::-1] #reverse the string   
sub_string = my_string[::2] #take every second character

#concatenate two or more strings: noi cac string
#concat strings with +: noi cac string bang dau +
#join element of a list into a string: .join()

#iterating
#iterating over a string by using for in loop: truy cap tung ky tu bang vong lap

#basic & useful function: ham co ban va huu ich
#strip() -> strip all whitespace characters from both end: xoa(remove) cac ki tu khoang trang o dau va cuoi string
#        -> or xoa ki tu bat ky: my_string.strip('O')
# split() -> tach cac xau con theo cac ki tu mong muon thanh list
# replace() -> thay the: "Help me".replace("me", "you")
# startswith('substring'): kiem tra chuoi co bat dau bang substring khong 
# endswith('substring'):  
# hoac kiem tra bat cu vi tri nao: index('substring'): tra ve index(neu khong co trong chuoi: return error)
# find('substring'): tuong tu index: nhung neu sunstring ko co trong chuoi thi tra ve -1
# title(): viet hoa cac chu cai dau
#capitalize(): viet hoa chu cai dau tien cua chuoi(neu la in hoa roi thi se chuyen thanh chu thuong)
#count('character'): dem xau co bao nhieu character

#string formating: ding dang chuoi
#use: %, .format(), f-Strings
#%: dinh dang bang toan tu
name = "Hung"
my_string = "I am %s" % name #s: string

pi = 3.14159
s = "pi number"
my_string = "Variable is %.2f from %s " % (pi, s) #%f: dinh dang tu float

#.format(): dinh danh bang format
age = 20
height = 165.9
my_string = "I am {} years old; {:.3f}".format(age, height)

#f-Strings: dinh dang bang f""
pi = 3.14159
my_string = f"Pi is {pi:.2f} and my name is {name}; {age} years old"
