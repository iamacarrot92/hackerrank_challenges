database = []
N = int(input())
for _ in range(N):
    name, *values= input().split()
    index_values = list(map(int, values)) 

    if name == "insert":
        database.insert(index_values[0], index_values[1])
    elif name == "print":
        print(database)
    elif name == "remove":
        database.remove(index_values[0])
    elif name == "append":
        database.append(index_values[0])
    elif name == "sort":
        database.sort()
    elif name == "pop":
        database.pop()
    elif name == "reverse":
        database.reverse()
