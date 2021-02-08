def mutate_string_method_one(string, position, character):
    list_string = list(string)
    list_string[position] = character
    return "".join(list_string)

def mutate_string_method_two(string, position, character):
    return string[:position] + character + string[positon + 1:]

s = input()
i, c = input().split()
method_one = mutate_string_method_one(s, int(i), c)
method_two = mutate_string_method_one(s, int(i), c)
print(method_one)
print(method_two)
