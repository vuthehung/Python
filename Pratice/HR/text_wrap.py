#khai bao thu vien: textwrap
import textwrap
#de bai: tach chuoi thanh cac chuoi con theo do dai
def wrap(string, max_width):
    s = textwrap.fill(string, max_width)
    return s
if __name__ == '__main__':
    s = input()
    w = int(input())
    res = wrap(s, w)
    print(res)
