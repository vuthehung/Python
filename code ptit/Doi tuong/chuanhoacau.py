while True:
    try:
        s = input().lower().split()
        a = [i for i in s]
        a[0] = a[0].title()
        
        if ( not(a[-1][-1] == "." or a[-1][-1] == "!" or a[-1][-1] == "?") ): a[-1] += "."
        elif ( len(a[-1]) == 1 ): 
            a[-2] += a[-1]
            a.pop(-1)
        
        print(*a)
    except: break