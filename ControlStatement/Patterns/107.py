'''

   1
  11
 1*1
1**1
11111

'''

for i in range(1,6):

    for k in range(1,5-i):
        print(" ",end="")
    for j in range(1,i+1):
        if i==5 or j==1 or i==j:
          print("1", end="")
        else:
          print("*",end="")
    print()