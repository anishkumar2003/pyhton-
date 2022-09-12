a=[]
n=int(input())
for i in range(1,n+1):
    c=int(input())
    a.append(c)
print(a)
f=max(a)
print(f)
a.remove(f)
print(a)
print(max(a))


if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
c=sum(student_marks[query_name])
d=c/3
z="{:.2f}".format(d)
print(z)
