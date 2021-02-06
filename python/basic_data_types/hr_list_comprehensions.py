def method_one(x, y, z, n):
    rand_grid = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if (i + j + k) != n:
                    rand_grid.append([i,j,k])
    return rand_grid

def method_two(x, y, z, n):
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if sum([i, j, k]) != n]


x = int(input())
y = int(input())
z = int(input())
n = int(input())

print(method_one(x, y, z, n))
print(method_two(x, y, z, n))

