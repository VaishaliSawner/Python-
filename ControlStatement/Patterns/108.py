'''

     A 
    AB
   A_C
   A__D
   ABCDE


'''
for i in range(1,6):

    for k in range(1,5-i):
        print(" ",end="")
    for j in range(1,i+1):
        if i==5 or j==1 or i==j:
          print(chr(j+64), end="")
        else:
          print("_",end="")
    print()