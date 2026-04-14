'''

     A 
    A  B 
   A  B  C 
  A  B  C  D 
 A  B  C  D  E 
'''
for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("",chr(j+64),"",end="")
    print()