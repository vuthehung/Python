
def solve():
    s1 = set(input().lower().split())
    s2 = set(input().lower().split())
    
    res1 = list(s1.union(s2))
    res2 = list(s1.intersection(s2))
    print(*(sorted(res1)))
    print(*(sorted(res2)))
    

def main():
    solve()

if __name__ == "__main__":
    main()