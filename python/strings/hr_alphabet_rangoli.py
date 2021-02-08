from string import ascii_letters as chars

def print_rangoli_method_one(size):
    new_list = []
    width = ((size)+(size -1)) + ((size - 1) + (size -1)) 
    result = ""
    if size <= 1:
       result = chars[0] 
    else:
        for x in range(0, size):
            new_list.append(("-".join(reversed(chars[x :size])) + "-" + "-".join(chars[x + 1:size])).center(width,'-')) 
        top = "\n".join(new_list[::-1])
        new_list.remove(new_list[0])
        bottom = "\n".join(new_list)
        result = top +"\n"+ bottom
    return result


n = int(input())
print(print_rangoli_method_one(n))
