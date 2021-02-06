def method_one(n):
    result = ""
    if n % 2 != 0:
        result = "Weird"
    elif range(2,5):
        result = "Not Weird"
    elif range(6,21):
        result = "Weird"
    else:
        result = "Not Weird"
    return result

def method_two(n):
    check = {True: "Not Weird", False: "Weird"}
    return check[n % 2== 0 and (n in range(2,6) or (n > 20))]

def method_three(n):
    result = ""
    if n % 2 == 0 and (n in range(2,6) or n > 20):
        result = "Not Weird"
    else:
        result = "Weird"
    return result

n = int(input())

print(method_one(n))
print(method_two(n))
print(method_three(n))

