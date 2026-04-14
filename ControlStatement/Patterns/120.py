
'''
     X 
    X  X 
   X  _  X 
  X  _  _  X 
 X  X  X  X  X 

'''

for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        if i==5 or j==1 or i==j:
            print("","X","",end="")
        else:
            print("","_","",end="")
    print()