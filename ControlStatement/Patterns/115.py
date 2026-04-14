'''

ABCDE
ABCD
 ABC
  AB
   A

'''
for i in range(5,0,-1):
    for k in range(1,5-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(chr(j+64),end="")
    print()