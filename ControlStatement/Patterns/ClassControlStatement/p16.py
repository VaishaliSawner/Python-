'''
   n = 1 to 5
   1 :- one
   2 :- two
   3 :- three
   4 :- four
   5 :- five

   if n == 1:
     print("one")
   elif n == 2:
     print("Two)
   elif n == 3:
     print("Three")
   elif n == 4:
     print("Four")
   elif n == 5
     print("Five")         
'''
n = int(input("Enter a number : "))
# n == a + b
match n:
 case 1: print("One")
 case 2: print("Two")
 case 3: print("First three...")
 case 3: print("Three")
 case 4: print("Four")
 case 5: print("Five")
 case _: print("Invalid value...")
 