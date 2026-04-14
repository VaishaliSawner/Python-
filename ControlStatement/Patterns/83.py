'''
a
bc
d f
g  j
klmno


'''
count=1

for i in range(6):
    for j in range(1,i+1):
        if(i==5 or j==1 or i==j):
            print(chr(count+96),end="")
            
        else:
            print(" ",end="")
        count=count+1
            
    print()


