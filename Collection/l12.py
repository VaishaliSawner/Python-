lst = [1,5,4,3,7,8,9,2]
#      0,1,2,3,4,5,6,7
k = 4
#    range(0,6)
print(f"Before {lst}")
for i in range(len(lst)-1):
  for j in range(i+1,len(lst)):
    if lst[i] > lst[j]:
        lst[i],lst[j] = lst[j],lst[i]

print(f"After {lst}")
print(f" {k}th largest element : {lst[len(lst)-k]}")
print(f"{k}th smallest element : {lst[k-1]}")