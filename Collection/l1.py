'''
  Indexing :- positive , indexing
'''
l1 = [10,20,30,40,50]
# len(l1) :--- 5
print(f"type of l1 {type(l1)}")
print(l1)

l1[0] = 1000
# help(class_name)
print(f"After change : {l1}")
#l1.insert(20,2000)
l1.insert(-20,5000)
print(f"After insert at 2nd : {l1}")
print(f"Total element available : {len(l1)}")
print(f"Value at 0th {l1[0]}")