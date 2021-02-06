def method_one(n, arr):
    arr_list = list(arr)
    arr_list_take_max = [arr_list[x] for x in range(n) if arr_list[x] != max(arr_list)]
    return max(arr_list_take_max)

n = int(input())
arr = map(int, input().split())

print(method_one)



