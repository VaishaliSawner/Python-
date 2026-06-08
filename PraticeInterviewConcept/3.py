'''

"Mutable default arguments are evaluated only once in Python.
So mutable objects like lists get shared across function calls
, which can cause unexpected behavior."
'''

def add_item(item, lst=[]):
 lst.append(item)
 return lst
print(add_item(1))
print(add_item(2))
'''
Output:
[1]
[1,2]
Reason:
Default mutable object created only once.
Correct way:
'''
def add_item(item, lst=None):
 if lst is None:
 lst = []
 lst.append(item)
 return lst



'''
Data Type  	Mutable/Immutable	Safe as Default Argument?
list	Mutable	❌ No
dict	Mutable	❌ No
set	Mutable	❌ No
tuple	Immutable	✔ Yes
int	Immutable	✔ Yes
string	Immutable	✔ Yes
None	Immutable	✔ Best
Best Practice


This happens because the same default list object is reused in every function call.

"Mutable default arguments like list, dict, and set can cause shared state
 problems because they are evaluated only once.
 Immutable objects like tuple and string are generally safe."
'''
