inli = list(map(int, input().split()))

c = '.|.'
d = '-'

top_design = []
bottom_design = []

for x in range(1,inli[0],2):
    top_design.append((c * x).center(inli[1], d))

for x in range(inli[0] -2,-1,-2):
    bottom_design.append((c * x).center(inli[1], d))

print("\n".join(top_design))    
print("WELCOME".center(inli[1],d))
print("\n".join(top_design[::-1]))    

