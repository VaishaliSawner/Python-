
for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,2*i):
        if i==5 or j==1 or j==2*i-1:
           print("*",end="")
        else:
            print("_",end="")
        
    print()