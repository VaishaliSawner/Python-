
'''

12345
1234
 123
  12
   1

'''



for i in range(6,1,-1):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i):
        print(j,end="")
    print()