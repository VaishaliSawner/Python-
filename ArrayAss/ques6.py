
# Sort array 
arr=[110,30,40,50,60]
print(arr)

for i in range (len(arr)):
    for j in range (i+1,len(arr)):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]


print(arr)




#li=[110,30,20,50,80,90]
#print(li)

#for i in range(len(li)):
  #  for j in range(i+1,len(li)):
     #  if li[i] > li[j]:
      #      li[i],li[j] = li[j],li[i]

#print(li)
