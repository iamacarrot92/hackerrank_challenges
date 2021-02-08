def swap_case_method_one(s):
    new_list = []
    for x in s:
        if x.isupper():
            new_list.append(x.lower())
        elif x.islower():
            new_list.append(x.upper())
        else:
            new_list.append(x)

    return "".join(new_list) 

def swap_case_method_two(s):
    return "".join([s.lower() if s.isupper() else s.upper() for s in s])
def swap_case_method_two(s):
    return s.swapcase()

s = input()
result_one = swap_case_method_one(s)
print(result_one)

result_two = swap_case_method_two(s)
print(result_two)

result_two = swap_case_method_two(s)
print(result_two)

