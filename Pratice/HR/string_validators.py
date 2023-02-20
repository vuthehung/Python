if __name__ == '__main__':
    s = input()
    #true: xau vua co so va chu
    print(any(c.isalnum() for c in s))
    #true: xau co chu
    print(any(c.isalpha() for c in s))
    #true: xau co so
    print(any(c.isdigit() for c in s))
    #true: xau co chu thuong
    print(any(c.islower() for c in s))
    #true: xau co chu hoa
    print(any(c.isupper() for c in s))