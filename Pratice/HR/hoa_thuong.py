def swap_case(s):
    new_s = ""
    for i in range(len(s)):
        if s[i].islower():
            new_s += s[i].upper()
        elif s[i].isupper():
            new_s += s[i].lower()
        else:
            new_s += s[i]
    return new_s
if __name__ == '__main__':
    s = input()
    res = swap_case(s)
    print(res)