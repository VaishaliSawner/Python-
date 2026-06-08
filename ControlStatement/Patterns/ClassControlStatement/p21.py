age = int(input("Enter age : "))

match age:
  case x if x <=10 : print("Child")
  case x if x > 10 and x <= 18: print("Teenage")
  case x if x > 18 and x <= 40: print("Young")
  case _: print("OLD IS GOLD")
  
# match age:
#  case x if x in range(1,11) : print("Child")
#  case x if x in range(11,19): print("Teenage")
#  case x if x in range(19,41): print("Young")
#  case _: print("OLD Is GOLD")