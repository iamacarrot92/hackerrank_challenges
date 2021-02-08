import textwrap

def wrap_method_one(string, max_width):
    list_wrapper = [] 
    for x in range(0,len(string),max_width):
        list_wrapper.append((string[x:(x+max_width)]))
    return "\n".join(list_wrapper)

def wrap_method_two(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

def wrap_method_three(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

string, max_width = input(), int(input())
result_one = wrap_method_one(string, max_width)
result_two = wrap_method_two(string, max_width)
result_three= wrap_method_three(string, max_width)

print(result_one)
print(result_two)
print(result_three)
