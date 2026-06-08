'''
  Positional
  Keyword
  Default
  Variable Length Argument

  Positional --> Default ---> Vairable Length-->Keword--> Varaible Length Keyword
  
'''
def f1(*a): # tuple
    sum = 0
    for item in a:
      print(item)  
      sum += item
    return sum  

result = f1(10,20,30,40,50,60)    
print(f"Sum : {result}")