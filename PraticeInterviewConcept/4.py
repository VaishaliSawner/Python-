 
'''
agar mein shallow copy mein kuch change karungi tuo original object mein affect hoga 

import copy 
a = [[1,2] , [3,4]]
b= copy.copy(a)
b[0][0] =100
print(a)
print(b)
'''

import copy
a = [[1,2],[3,4]]
b = copy.deepcopy(a)
print(a)

