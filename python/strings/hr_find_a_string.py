def count_substring_method_one(string, sub_string):
    count = 0
    for x in range(len(string)):
        if sub_string == string[x:x+len(sub_string)]:
            count += 1
        elif len(string[x:x+len(sub_string)]) < len(sub_string):
            break
    return count

def count_substring_method_two(string, sub_string):
    count = 0
    for x in range(len(string)):
        if string[x:].startswith(sub_string):
            count += 1
    return count

def count_substring_method_three(string, sub_string):
    count = 0
    while sub_string in string:
        count += 1
        string = string[string.find(sub_string) + 1:]
    return count

string = input().strip()
sub_string = input().strip()

count_method_one = count_substring_method_one(string, sub_string)
print(count_method_one)
count_method_two = count_substring_method_two(string, sub_string)
print(count_method_two)
count_method_three = count_substring_method_three(string, sub_string)
print(count_method_three)
