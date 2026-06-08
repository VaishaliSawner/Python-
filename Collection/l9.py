lst = [-100,20,50,12,54,78,21,1000]


min = float('inf')
max = float('-inf')


for element in lst: # 1
    if element >= max:
        max = element
    if element <= min:
        min = element    
else:
    print(f"Max {max} and Min {min}")    