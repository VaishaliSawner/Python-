'''
term = 1 	2	 4	 7	 11	 16 	…… n terms
difference =   1   2    3

'''

n = int(input("Enter number of terms : "))

term = 1
difference = 1
for i in range(1,n+1):
  print(term,end=" ")
  term += difference
  difference += 1  

print()