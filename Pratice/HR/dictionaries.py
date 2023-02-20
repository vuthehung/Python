if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    mark = student_marks.get(query_name)
    res = 0
    for i in range(len(mark)):
        res += mark[i]
    res /= len(mark)
    
    print("{:.2f}".format(res))