def split_and_join_method_one(line):
    return "-".join(line)

line = input().split()
result_one = split_and_join_method_one(line)

print(result_one)
print(*line, sep="-")
