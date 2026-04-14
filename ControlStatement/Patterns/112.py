'''

12345
1__4
 1_3
  12
   1


'''

for i in range(5,0,-1):
    for k in range(1,5-i):
        print(" ",end="")
    for j in range(1,i+1):
        if i==5 or j==1 or i==j:
            print(j,end="")
        else:
            print("_",end="")
    print()