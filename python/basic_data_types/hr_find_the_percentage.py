def method_one(query_name, student_marks):
    for key,value in student_marks.items():
        if key == query_name:
            print("{:.2f}".format(sum(value)/ len(value)))

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

method_one(query_name, student_marks)

