# AABCAAADA
# 3

def remove_dups(l):
   for a in l:
      new_l = []
      for b in a:
          if b not in new_l:
             new_l.append(b)
      yield new_l

def merge_the_tools_one(string, k):
    substrings_list = [string[x:x+k] for x in range(0, len(string), k)]
    # print(remove_dups(substrings_list))
    for x in substrings_list:
        new_l = []
        for y in x:
            if y not in new_l:
                new_l.append(y)

        print("".join(new_l))

def merge_the_tools_two(string, k):
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            print(''.join(temp))
            temp = []
            len_temp = 0

def merge_the_tools_three(string, k):
    for i in range(0, len(string), k):
        s = ""
        for j in string[i: i + k]:
            if j not in s:
                s += j
        print(s)

string, k = input(), int(input())
merge_the_tools_one(string, k)


