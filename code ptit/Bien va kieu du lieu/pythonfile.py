
def solve():
    s = input()
    if len(s) < 3:
        print("nos")
    else:
        ten, mo_rong = s.split('.')
        mo_rong = mo_rong.lower()
        if mo_rong == "py":
            print("yes")
        else:
            print("no")

def main():
    solve()

if __name__ == "__main__":
    main()