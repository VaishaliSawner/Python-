lst = [1,2,3,4,5,7,9,10,20,50,90,76,89,23,45]

#result = [x*x for x in lst]

#result = [ x*x for x in lst if x%2==1]
#result = [ x*x for x in lst if x%2==1 and x > 1]
print(lst)
#result = [x*x*x if x%2  else x*x for x in lst]
element = 50

list1 = [x for x in lst if x > element]
list2 = [x for x in lst if x < element]

print(list1)
print(list2)