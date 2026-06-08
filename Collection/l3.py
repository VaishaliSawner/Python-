'''
  append()
  insert()
  pop()
  remove()
  reverse()
  count()
  clear()
  --------
  len() -- function
  index()
'''

l1 = [10,20,10,40,50]

# 60,70,80
#l1.append([60,70,80])
l1.extend([60,70,80])
print(l1)
#index_value = l1.index(10,1)
#print(f"Index value : {index_value}")