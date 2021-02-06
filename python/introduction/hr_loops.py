def method_one(n):
    for x in range(n):
        print(x * x)
        

def method_two(n):
    return [print(i**2) for i in range(n)]


def method_three(n):
    square = [x ** 2 for x in range(n)]
    print(*squares, sep="\n")


n = int(input())

method_one(n)
method_two(n)
method_three(n)
