def method_one(n):
    '''
    result = []
    for x in range(n):
       result.append(x) 
    return "".join(map(str,result)) 

    '''
    return "".join([str(x) for x in range(1,n + 1)])

def method_two(n):
    '''
    for i in range(1, n +1):
        print(i,end="")
    '''
    print(*range(1,int(input()+1)),sep='')

def method_three(n):
    [print(i,end='') for i in range(1,n + 1)]

n = int(input())
print(method_one(n))
method_two(n)

