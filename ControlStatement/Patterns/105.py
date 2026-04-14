'''
      5
     44
    333
   2222
  11111
   

'''

for i in range(5, 0, -1):

    for k in range(1,i-1):
        print(" ",end="")
    for j in range(6 - i):
        print(i, end="")
    print()