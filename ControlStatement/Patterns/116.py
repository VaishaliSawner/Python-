'''

11111
 2222
  333
   44
    5
'''

for i in range(1,6):
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,6-i+1):
        print(i,end="")
    print()


