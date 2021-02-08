import string
def solve_method_one(s):
    s_split = s.split(' ')
    s_split_transform = []
    for x in s_split:
        s_split_transform.append(x.capitalize())
    return " ".join(s_split_transform)

def solve_method_two(s):
    s_split = s.split(' ')
    return " ".join([word.capitalize() for word in s_split])

def solve_method_three(s):
    return string.capwords(s, ' ')

def solve_method_four(s):
    return ' '.join(map(str.capitalize, s.split(' ')))
    
s = input()
print(solve_method_one(s))
print(solve_method_two(s))
print(solve_method_three(s))
print(solve_method_four(s))
