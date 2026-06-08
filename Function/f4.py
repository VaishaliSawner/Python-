def modify(a): # a = (1,2,[3,4])
    a[2].append(5)
    pass

x = (1,2,[3,4])

print(f"Before modify  :{x}")
modify(x)
print(f"After modify : {x}")