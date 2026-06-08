n = int(input("Enter a number : "))
match n:
  case x if x%2 ==0 : print(f"{x} : Even")
  case _:print("ODD")

# match n%2:
#   case 0: print("Even")
#   #case 1: print("Odd")
#   case _:print("Odd")