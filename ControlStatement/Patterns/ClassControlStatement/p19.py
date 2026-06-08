value = 1
value = 1.5
value = False
value = None
value = 2 + 5j
value = ""
value = [1,2,3]
value  = (1,2)
value = {"a": 100}
value = {1,2}
value = b"ABC"
value = 0B00001

match value:
 #case {1}: print("Set matched....") Error :- set not allowed in match case
 case b"ABC": print("byte string matched...")
 case {} : print("Empty dict matched..")
 case {"a": 100}: print("Dict matched with data...")
 case (1,2): print("Type matched with data...")
 case (): print("Tuple matched...") 
 case [1,2,3]: print("List matched with data...")
 case []: print("List matched..")
 case "":print("Empty string matched...")
 case "Dear Students": print("String Mathced..")
 case 2 + 5j: print("Complex matched..")
 case None: print("None Matched...")
 case False: print("False | Boolean Matched...")
 case 1: print("1 | int matched..")
 case 1.5: print("1.5 | float matched ")
 case _: print(f"{value} not matched..")