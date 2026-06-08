'''
   -6	-3	0	3	6	9	……. n terms 

'''

n = int(input("Enter number of terms : "))

if n%3 == 0 and n > 0:
  for i in range(-n,n+1,3):
    print(i,end=" ")
  else:
    print() 
else:
  print("{} must be divisible by 3 and must be positive".format(n))     

