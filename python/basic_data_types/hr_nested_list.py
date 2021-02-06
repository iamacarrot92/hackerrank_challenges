students = {}
scores = []
def method_one(scores, students):
    scores_min = [x for x in scores if x != min(scores)]
    result = []
    for key,value in students.items():
        if value == min(scores_min):
            result.append(key)
    return "\n".join(sorted(result))

for _ in range(int(input())):
    name = input()
    score = float(input())
    scores.append(score)
    students[name] = score

print(method_one(scores, students))


def method_two(a):
    a.sort()
    b = [i for i in a if i[0] != a[0][0]]
    c = [j for j in b if j[0] == b[0][0]]
    result = []
    for i in range(len(c)):
       result.append(c[i][1]) 
    return result

a = []
for _ in range(int(input())):
    name_a = input()
    score_a = float(input())
    a.append([score_a, name_a])

print(method_two(a))

    
