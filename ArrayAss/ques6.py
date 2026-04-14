li=[110,30,20,50,80,90]
print(li)

for i in range(len(li)):
    for j in range(i+1,len(li)):
       if li[i] > li[j]:
            li[i],li[j] = li[j],li[i]

print(li)
