
from queue import Queue

def solve():
    t = int(input())
    q = Queue()
    q.put('0')
    q.put('2')
    q.put('4')
    q.put('6')
    q.put('8')
    a = set()
    while not(q.empty()):
        tmp = q.get()
        if tmp[0] != '0' and len(tmp) % 2 == 0:
            a.add(int(tmp))
        if len(tmp) < 6:
            if len(tmp) < 4:
                q.put(tmp + tmp[::-1])
            q.put('0' + tmp + '0')
            q.put('2' + tmp + '2')
            q.put('4' + tmp + '4')
            q.put('6' + tmp + '6')
            q.put('8' + tmp + '8')
    a = sorted(a)
    for _ in range(t):
        n = int(input())
        for i in a:
            if i < n:
                print(i, end= ' ')
            else:
                break
        print()

def main():
    solve()

if __name__ == "__main__":
    main()