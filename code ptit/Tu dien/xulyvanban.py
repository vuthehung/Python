

def solve():
    text = ""
    while True:
        try:
            str = input() 
            if len(str) == 0: break
            text += " " + str
        except EOFError:
            break
    tmp = ''
    for i in range(len(text)):
        if text[i] == '!' or text[i] == '?' or text[i] == '.':
            tmp += '.'
        else:
            tmp += text[i]
    a = list(tmp.split('.'))
    res = []
    for i in a:
        a_i = list(i.split())
        s = ' '.join(a_i)
        res.append(s.capitalize())
    for i in res:
        print(i)
    
def main():
    solve()

if __name__ == "__main__":
    main()